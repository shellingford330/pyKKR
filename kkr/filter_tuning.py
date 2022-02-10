import numpy as np

from .kernels import ExponentialQuadraticKernel

from .filter import KernelKalmanFilter

# args: X1, X2, Y2, X0, observations, bk, bg, alpha_t, alpha_o, alpha_q
def tuning_kernel_kalman_filter(args):
  X1 = args[0]
  X2 = args[1]
  Y2 = args[2]
  X0 = args[3]
  observations = args[4]
  bk = args[5]
  bg = args[6]
  alpha_t = args[7]
  alpha_o = args[8]
  alpha_q = args[9]
  observation_dim = args[10]

  # kernel function k         
  kernel_k = ExponentialQuadraticKernel()
  kernel_k.bandwidth = bk
  kernel_k.normalized = True

  # kernel function g
  kernel_g = ExponentialQuadraticKernel()
  kernel_g.bandwidth = bg
  kernel_g.normalized = True

  KKF = KernelKalmanFilter(X1, X2, Y2, X0)
  KKF.kernel_k = kernel_k
  KKF.kernel_g = kernel_g
  KKF.alpha_t = alpha_t
  KKF.alpha_o = alpha_o
  KKF.alpha_q = alpha_q

  KKF.learn_model()

  mu, Sigma = KKF.filter(observations)

  filtered = np.moveaxis(mu, 2, 0).reshape(-1, observation_dim)
  return filtered
