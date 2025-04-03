import simpy, random

def passenger(env, id_check, personal_scanners, wait_times):
    arrival_time = env.now
    with id_check.request() as req:
        yield req
        start_id = env.now
        yield env.timeout(random.expovariate(1.0/0.75))
    finish_id = env.now
    shortest_queue = min(personal_scanners, key=lambda r: len(r.queue))
    with shortest_queue.request() as req2:
        yield req2
        start_scan = env.now
        yield env.timeout(random.uniform(0.5, 1.0))
    finish_scan = env.now
    wait_id = start_id - arrival_time
    wait_scan = start_scan - finish_id
    total_wait = wait_id + wait_scan
    wait_times.append(total_wait)

def run_simulation(num_checkers, num_scanners, lam1, sim_duration):
    random.seed(0)
    env = simpy.Environment()
    id_check = simpy.Resource(env, capacity=num_checkers)
    personal_scanners = [simpy.Resource(env, capacity=1) for _ in range(num_scanners)]
    wait_times = []
    def generate_arrivals():
        while True:
            interarrival = random.expovariate(lam1)
            yield env.timeout(interarrival)
            env.process(passenger(env, id_check, personal_scanners, wait_times))
    env.process(generate_arrivals())
    env.run(until=sim_duration)
    return wait_times

wait_times = run_simulation(num_checkers=36, num_scanners=36, lam1=50, sim_duration=1000)
print(f"Avg wait = {sum(wait_times)/len(wait_times):.2f} minutes")
wait_times = run_simulation(num_checkers=37, num_scanners=37, lam1=50, sim_duration=1000)
print(f"Avg wait = {sum(wait_times)/len(wait_times):.2f} minutes")
wait_times = run_simulation(num_checkers=38, num_scanners=38, lam1=50, sim_duration=1000)
print(f"Avg wait = {sum(wait_times)/len(wait_times):.2f} minutes")
