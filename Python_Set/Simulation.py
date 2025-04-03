import simpy
import random
from statistics import mean

random.seed(42)

def passenger(env, id_check, personal_queues, stats, sim_time):
    arrival_time = env.now
    if arrival_time > sim_time:
        return
    # ID check process
    with id_check.request() as request:
        yield request
        wait_id = env.now - arrival_time
        service_time_id = random.expovariate(0.75)  # Mean service time = 1/0.75 ≈ 1.333 mins
        yield env.timeout(service_time_id)
    exit_id_time = env.now
    # Personal check process
    # Find the shortest queue
    queue_lengths = [len(queue.queue) for queue in personal_queues]
    shortest_idx = queue_lengths.index(min(queue_lengths))
    chosen_queue = personal_queues[shortest_idx]
    with chosen_queue.request() as request:
        yield request
        wait_personal = env.now - exit_id_time
        service_time_personal = random.uniform(0.5, 1.0)
        yield env.timeout(service_time_personal)
    # Record wait times
    stats['total_waits'].append(wait_id + wait_personal)
    stats['wait_id'].append(wait_id)
    stats['wait_personal'].append(wait_personal)

def passenger_generator(env, id_check, personal_queues, stats, sim_time):
    while True:
        yield env.timeout(random.expovariate(5))  # λ1 = 5 arrivals/minute
        env.process(passenger(env, id_check, personal_queues, stats, sim_time))

def run_simulation(n_servers_id, n_personal_queues, sim_time=10080):
    env = simpy.Environment()
    stats = {
        'total_waits': [],
        'wait_id': [],
        'wait_personal': []
    }
    # Create resources
    id_check = simpy.Resource(env, capacity=n_servers_id)
    personal_queues = [simpy.Resource(env, capacity=1) for _ in range(n_personal_queues)]
    # Start passenger generator
    env.process(passenger_generator(env, id_check, personal_queues, stats, sim_time))
    # Run simulation (with buffer time to process remaining passengers)
    env.run(until=sim_time + 1440)  # Extend time to clear queues
    # Calculate average waits
    avg_total = mean(stats['total_waits']) if stats['total_waits'] else 0
    avg_id = mean(stats['wait_id']) if stats['wait_id'] else 0
    avg_personal = mean(stats['wait_personal']) if stats['wait_personal'] else 0
    return avg_total, avg_id, avg_personal

# Example: Test with 7 ID checkers and 10 personal-check queues
n_servers_id = 3
n_personal_queues = 3
avg_total, avg_id, avg_personal = run_simulation(n_servers_id, n_personal_queues)
print(f"ID Checkers: {n_servers_id}, Personal Queues: {n_personal_queues}")
print(f"Average Total Wait: {avg_total:.2f} mins")
print(f"  Breakdown: ID Check = {avg_id:.2f} mins, Personal Check = {avg_personal:.2f} mins")