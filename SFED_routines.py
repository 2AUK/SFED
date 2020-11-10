from gridData import Grid, OpenDX
import numpy as np

kB=0.00198721587 #CONSTANT
NA=6.022142E23 #CONSTANT

np.set_printoptions(suppress=True)

def mu_gf_3drism(h_o, c_o, h_h, c_h, d, rho=0.03342285869, kB=0.00198721587, T=300, Na=6.022142E23):
    mu = rho * np.sum(-0.5 * h_o * c_o - c_o) * d + 2 * rho * np.sum(-0.5 * h_h * c_h - c_h) * d
    return mu*kB*T

def mu_kh_3drism(h_o, c_o, h_h, c_h, d, rho=0.03342285869, kB=0.00198721587, T=300, Na=6.022142E23):
    mu = rho*np.sum(0.5*np.power(h_o, 2)*np.heaviside(-h_o, 1) - 0.5*h_o*c_o - c_o)*d + 2*rho*np.sum(0.5*np.power(h_h, 2)*np.heaviside(-h_h, 0.5) - 0.5*h_h*c_h - c_h)*d
    return mu*kB*T

def sfed_gf_3drism(h_o, c_o, h_h, c_h, rho=0.03332834, kB=1.9872041E-3, T=298.15, Na=6.022142E23):
    wr = rho * (-0.5 * h_o * c_o - c_o) + 2 * rho * (-0.5 * h_h * c_h - c_h)
    return wr*kB*T

def sfed_hnc_3drism(h_o, c_o, h_h, c_h, rho=0.03332834, kB=1.9872041E-3, T=298.15, Na=6.022142E23):
    wr = (-0.5 * h_o * (c_o - h_o)) - c_o + 2 * rho * (-0.5 * h_h * (c_h - h_h)) - c_h
    return wr*kB*T

def sfed_kh_3drism(h_o, c_o, h_h, c_h, rho=0.03342285869, kB=0.00198721587, T=300, Na=6.022142E23):
    wr = rho*(0.5*np.power(h_o, 2)*np.heaviside(-h_o, 1) - 0.5*h_o*c_o - c_o) + 2*rho*(0.5*np.power(h_h, 2)*np.heaviside(-h_h, 0.5) - 0.5*h_h*c_h - c_h)
    return wr*kB*T

def sfed_psen_3drism(h_o, c_o, h_h, c_h, u_o, u_h, n, rho=0.03342285869, kB=0.00198721587, T=300, Na=6.022142E23):
    ts_o = u_o + h_o - c_o
    ts_h = u_h + h_h - c_h
    hnc = sfed_hnc_3drism(h_o, c_o, h_h, c_h, rho, kB, T, Na)
    wr = hnc - (rho*np.heaviside(h_o)*np.power(ts_o, n+1)/np.math.factorial(n+1) + 2*rho*np.heaviside(h_h)*np.power(ts_h, n+1)/np.math.factorial(n+1))
    return wr*kB*T

def mu_kh_3drism_g(g_o, c_o, g_h, c_h, d, rho=0.03342285869, kB=0.00198721587, T=300, Na=6.022142E23):
    h_o = g_o - 1.0
    h_h = g_h - 1.0
    mu = rho*np.sum(0.5*np.power(h_o, 2)*np.heaviside(-h_o, 1) - 0.5*h_o*c_o - c_o)*d + 2*rho*np.sum(0.5*np.power(h_h, 2)*np.heaviside(-h_h, 0.5) - 0.5*h_h*c_h - c_h)*d
    return mu*kB*T

def sfed_kh_3drism_g(g_o, c_o, g_h, c_h, rho=0.03342285869, kB=0.00198721587, T=300, Na=6.022142E23):
    h_o = g_o - 1.0
    h_h = g_h - 1.0
    wr = rho*(0.5*np.power(h_o, 2)*np.heaviside(-h_o, 1) - 0.5*h_o*c_o - c_o) + 2*rho*(0.5*np.power(h_h, 2)*np.heaviside(-h_h, 0.5) - 0.5*h_h*c_h - c_h)
    return wr*kB*T

def sfed_gf_3drism_g(h_o, c_o, h_h, c_h, rho=0.03332834, kB=1.9872041E-3, T=300, Na=6.022142E23):
    h_o = g_o - 1.0
    h_h = g_h - 1.0
    wr = rho * (-0.5 * h_o * c_o - c_o) + 2 * rho * (-0.5 * h_h * c_h - c_h)
    return wr*kB*T

def integrate_sfed(sfed, d):
    return np.sum(sfed * d)

def writedx(sfed_o, ho, fname):
    sfed = OpenDX.field('SFED')
    sfed.add('positions', OpenDX.gridpositions(1, sfed_o.shape, ho.origin, ho.delta))
    sfed.add('connections', OpenDX.gridconnections(2, sfed_o.shape))
    sfed.add('data', OpenDX.array(3, sfed_o))
    sfed.write(fname + ".dx")