import numpy as np
import pylab as plt


def distributions(m_a=10, m_b=10, m_c=25):
    dist_a = []
    dist_b = []
    dist_c = []
    for i in range(100):
        dist_a.append(np.random.randn(2) + m_a)
        dist_c.append(np.random.randn(2) + m_c)
        dist_b.append(np.random.randn(2) * 5.5 + m_b)

    return dist_a, dist_b, dist_c


dist_a, dist_b, dist_c = distributions()


# plotting the distributions
plt.scatter([a for a, _ in dist_a], [
            b for _, b in dist_a], label='distribution A')
plt.scatter([a for a, _ in dist_b], [
            b for _, b in dist_b], label='distribution B')
plt.scatter([a for a, _ in dist_c], [
            b for _, b in dist_c], label='distribution C')
plt.legend()

# calculate baricenters
bc_a = np.mean(dist_a, axis=0)
bc_b = np.mean(dist_b, axis=0)
bc_c = np.mean(dist_c, axis=0)

# calculate the distance between baricenters
dist_a_b = np.linalg.norm(bc_a-bc_b)
dist_a_c = np.linalg.norm(bc_a-bc_c)
dist_b_c = np.linalg.norm(bc_b-bc_c)

print("baricenter distante between distribution A and distribution B=", dist_a_b)
print("baricenter distante between distribution A and distribution C=", dist_a_c)
print("baricenter distante between distribution B and distribution C=", dist_b_c)
print("\n")

# calculate the spread of the distributions, e.g. their standard deviation
spread_a = np.std(dist_a)
spread_b = np.std(dist_b)
spread_c = np.std(dist_c)


dist_spread_a_b = np.abs(spread_a-spread_b)
dist_spread_a_c = np.abs(spread_a-spread_c)
dist_spread_b_c = np.abs(spread_b-spread_c)

print("spread distance between distribution A and distribution B=", dist_spread_a_b)
print("spread distance between distribution A and distribution C=", dist_spread_a_c)
print("spread distance between of distribution B and distribution C=", dist_spread_b_c)
print("\n")

# put in a single metric. NB, the paramenter of this join is subjective, and depend on the usecase
# alpha=0 : don't care about the euclidean distance between the baricenters
# alpha=1 : don't care about the spread distance between the baricenters

alpha = 0.3
joint_metric_a_b = alpha*dist_a_b + (1-alpha)*dist_spread_a_b
joint_metric_a_c = alpha*dist_a_c + (1-alpha)*dist_spread_a_c
joint_metric_b_c = alpha*dist_b_c + (1-alpha)*dist_spread_b_c


print("joined metric distance between distribution A and distribution B=",
      joint_metric_a_b)
print("joined metric distance between distribution A and distribution C=",
      joint_metric_a_c)
print("joined metric distance between distribution B and distribution C=",
      joint_metric_b_c)
plt.show()
