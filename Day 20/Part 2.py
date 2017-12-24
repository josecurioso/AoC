class Particle:
    def __init__(self, p, v, a):
        self.p = [int(x) for x in p[3:-1].split(",")]
        self.v = [int(x) for x in v[3:-1].split(",")]
        self.a = [int(x) for x in a[3:-1].split(",")]
        self.dead = False

    def update(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        self.v[2] += self.a[2]
        self.p[0] += self.v[0]
        self.p[1] += self.v[1]
        self.p[2] += self.v[2]

    def get_position(self):
        return(self.p)

    def get_distance(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

    def get_velocity(self):
        return abs(self.v[0]) + abs(self.v[1]) + abs(self.v[2])

    def get_accel(self):
        return abs(self.a[0]) + abs(self.a[1]) + abs(self.a[2])

    def kill(self):
        self.dead = True

    def alive(self):
        if self.dead:
            return False
        return True


particles = []
with open("input.txt","r") as fh:
    for i, line in enumerate(fh.readlines()):
        p, v, a = line.strip().split(", ")
        particles.append(Particle(p, v, a))

cycle = 0
last_killed = 0
while cycle < last_killed + 100:
    positions = []
    for x in range(len(particles)):
        if particles[x].alive():
            particles[x].update()
            pos = particles[x].get_position()
            positions.append(pos)
    for x in range(len(particles)):
        if particles[x].alive():
            pos = particles[x].get_position()
            if positions.count(pos) > 1:
                particles[x].kill()
                last_killed = cycle
    cycle += 1

count = 0
for i in range(len(particles)):
    part = particles[i]
    if part.alive():
        count += 1

print(count)
