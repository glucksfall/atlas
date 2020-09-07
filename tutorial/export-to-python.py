# exported from PySB model 'atlas_rbm.construct_model_from_metabolic_network'

import numpy
import scipy.integrate
import collections
import itertools
import distutils.errors


_use_inline = False
# try to inline a C statement to see if inline is functional
try:
    import weave
    weave.inline('int i;', force=1)
    _use_inline = True
except ImportError:
    pass
except distutils.errors.CompileError:
    pass

Parameter = collections.namedtuple('Parameter', 'name value')
Observable = collections.namedtuple('Observable', 'name species coefficients')
Initial = collections.namedtuple('Initial', 'param_index species_index')


class Model(object):
    
    def __init__(self):
        self.y = None
        self.yobs = None
        self.integrator = scipy.integrate.ode(self.ode_rhs)
        self.integrator.set_integrator('vode', method='bdf',
                                       with_jacobian=True)
        self.y0 = numpy.empty(27)
        self.ydot = numpy.empty(27)
        self.sim_param_values = numpy.empty(43)
        self.parameters = [None] * 43
        self.observables = [None] * 20
        self.initials = [None] * 23
    
        self.parameters[0] = Parameter('t0_met_ACETYL_COA_cyt', 0)
        self.parameters[1] = Parameter('t0_met_ALLOLACTOSE_cyt', 0)
        self.parameters[2] = Parameter('t0_met_Alpha_lactose_cyt', 0)
        self.parameters[3] = Parameter('t0_met_Beta_D_Galactosides_cyt', 0)
        self.parameters[4] = Parameter('t0_met_CO_A_cyt', 0)
        self.parameters[5] = Parameter('t0_met_CPD_15972_cyt', 0)
        self.parameters[6] = Parameter('t0_met_CPD_3561_cyt', 0)
        self.parameters[7] = Parameter('t0_met_CPD_3785_cyt', 0)
        self.parameters[8] = Parameter('t0_met_CPD_3801_cyt', 0)
        self.parameters[9] = Parameter('t0_met_D_ARABINOSE_cyt', 0)
        self.parameters[10] = Parameter('t0_met_Fructofuranose_cyt', 0)
        self.parameters[11] = Parameter('t0_met_GALACTOSE_cyt', 0)
        self.parameters[12] = Parameter('t0_met_Glucopyranose_cyt', 0)
        self.parameters[13] = Parameter('t0_met_MELIBIOSE_cyt', 0)
        self.parameters[14] = Parameter('t0_met_PROTON_cyt', 0)
        self.parameters[15] = Parameter('t0_met_WATER_cyt', 100)
        self.parameters[16] = Parameter('t0_met__6_Acetyl_Beta_D_Galactosides_cyt', 0)
        self.parameters[17] = Parameter('t0_prot_lacA_cyt', 0)
        self.parameters[18] = Parameter('t0_prot_lacY_cyt', 0)
        self.parameters[19] = Parameter('t0_prot_lacZ_cyt', 1)
        self.parameters[20] = Parameter('fwd_GALACTOACETYLTRAN_RXN', 1)
        self.parameters[21] = Parameter('rvs_GALACTOACETYLTRAN_RXN', 0)
        self.parameters[22] = Parameter('fwd_TRANS_RXN_24', 1)
        self.parameters[23] = Parameter('rvs_TRANS_RXN_24', 0)
        self.parameters[24] = Parameter('fwd_TRANS_RXN_94', 1)
        self.parameters[25] = Parameter('rvs_TRANS_RXN_94', 0)
        self.parameters[26] = Parameter('fwd_RXN0_7215', 1)
        self.parameters[27] = Parameter('rvs_RXN0_7215', 0)
        self.parameters[28] = Parameter('fwd_RXN0_7217', 1)
        self.parameters[29] = Parameter('rvs_RXN0_7217', 0)
        self.parameters[30] = Parameter('fwd_RXN_17755', 1)
        self.parameters[31] = Parameter('rvs_RXN_17755', 0)
        self.parameters[32] = Parameter('fwd_BETAGALACTOSID_RXN', 1)
        self.parameters[33] = Parameter('rvs_BETAGALACTOSID_RXN', 0)
        self.parameters[34] = Parameter('fwd_RXN0_5363', 1)
        self.parameters[35] = Parameter('rvs_RXN0_5363', 1)
        self.parameters[36] = Parameter('fwd_RXN_17726', 1)
        self.parameters[37] = Parameter('rvs_RXN_17726', 0)
        self.parameters[38] = Parameter('fwd_RXN0_7219', 1)
        self.parameters[39] = Parameter('rvs_RXN0_7219', 0)
        self.parameters[40] = Parameter('t0_dna_Alpha_lactose_per', 100)
        self.parameters[41] = Parameter('t0_dna_PROTON_per', 100)
        self.parameters[42] = Parameter('t0_prot_lacY_imem', 1)

        self.observables[0] = Observable('obs_met_ACETYL_COA_cyt', [0], [1])
        self.observables[1] = Observable('obs_met_ALLOLACTOSE_cyt', [1], [1])
        self.observables[2] = Observable('obs_met_Alpha_lactose_cyt', [2], [1])
        self.observables[3] = Observable('obs_met_Beta_D_Galactosides_cyt', [3], [1])
        self.observables[4] = Observable('obs_met_CO_A_cyt', [4], [1])
        self.observables[5] = Observable('obs_met_CPD_15972_cyt', [5], [1])
        self.observables[6] = Observable('obs_met_CPD_3561_cyt', [6], [1])
        self.observables[7] = Observable('obs_met_CPD_3785_cyt', [7], [1])
        self.observables[8] = Observable('obs_met_CPD_3801_cyt', [8], [1])
        self.observables[9] = Observable('obs_met_D_ARABINOSE_cyt', [9], [1])
        self.observables[10] = Observable('obs_met_Fructofuranose_cyt', [10], [1])
        self.observables[11] = Observable('obs_met_GALACTOSE_cyt', [11], [1])
        self.observables[12] = Observable('obs_met_Glucopyranose_cyt', [12], [1])
        self.observables[13] = Observable('obs_met_MELIBIOSE_cyt', [13], [1])
        self.observables[14] = Observable('obs_met_PROTON_cyt', [14], [1])
        self.observables[15] = Observable('obs_met_WATER_cyt', [15], [1])
        self.observables[16] = Observable('obs_met__6_Acetyl_Beta_D_Galactosides_cyt', [16], [1])
        self.observables[17] = Observable('obs_met_Alpha_lactose_per', [20], [1])
        self.observables[18] = Observable('obs_met_PROTON_per', [21], [1])
        self.observables[19] = Observable('obs_prot_lacY_imem', [22], [1])

        self.initials[0] = Initial(0, 0)
        self.initials[1] = Initial(1, 1)
        self.initials[2] = Initial(2, 2)
        self.initials[3] = Initial(3, 3)
        self.initials[4] = Initial(4, 4)
        self.initials[5] = Initial(5, 5)
        self.initials[6] = Initial(6, 6)
        self.initials[7] = Initial(7, 7)
        self.initials[8] = Initial(8, 8)
        self.initials[9] = Initial(9, 9)
        self.initials[10] = Initial(10, 10)
        self.initials[11] = Initial(11, 11)
        self.initials[12] = Initial(12, 12)
        self.initials[13] = Initial(13, 13)
        self.initials[14] = Initial(14, 14)
        self.initials[15] = Initial(15, 15)
        self.initials[16] = Initial(16, 16)
        self.initials[17] = Initial(17, 17)
        self.initials[18] = Initial(18, 18)
        self.initials[19] = Initial(19, 19)
        self.initials[20] = Initial(40, 20)
        self.initials[21] = Initial(41, 21)
        self.initials[22] = Initial(42, 22)

    if _use_inline:
        
        def ode_rhs(self, t, y, p):
            ydot = self.ydot
            weave.inline(r'''
                ydot[0] = y[16]*y[17]*y[4]*p[21] + (y[0]*y[17]*y[3]*p[20])*(-1);
                ydot[1] = y[19]*y[2]*p[34] + (y[1]*y[19]*p[35])*(-1);
                ydot[2] = y[1]*y[19]*p[35] + y[20]*y[21]*y[22]*p[22] + (y[19]*y[2]*p[34])*(-1) + (y[14]*y[2]*y[22]*p[23])*(-1);
                ydot[3] = y[16]*y[17]*y[4]*p[21] + (y[0]*y[17]*y[3]*p[20])*(-1);
                ydot[4] = y[0]*y[17]*y[3]*p[20] + (y[16]*y[17]*y[4]*p[21])*(-1);
                ydot[5] = y[11]*y[12]*y[19]*p[33] + (y[15]*y[19]*y[5]*p[32])*(-1);
                ydot[6] = y[10]*y[11]*y[19]*p[37] + y[21]*y[22]*y[24]*p[26] + (y[14]*y[22]*y[6]*p[27])*(-1) + (y[15]*y[19]*y[6]*p[36])*(-1);
                ydot[7] = y[11]*y[19]*y[9]*p[39] + y[21]*y[22]*y[25]*p[28] + (y[14]*y[22]*y[7]*p[29])*(-1) + (y[15]*y[19]*y[7]*p[38])*(-1);
                ydot[8] = y[21]*y[22]*y[26]*p[30] + (y[14]*y[22]*y[8]*p[31])*(-1);
                ydot[9] = y[15]*y[19]*y[7]*p[38] + (y[11]*y[19]*y[9]*p[39])*(-1);
                ydot[10] = y[15]*y[19]*y[6]*p[36] + (y[10]*y[11]*y[19]*p[37])*(-1);
                ydot[11] = y[15]*y[19]*y[5]*p[32] + y[15]*y[19]*y[6]*p[36] + y[15]*y[19]*y[7]*p[38] + (y[10]*y[11]*y[19]*p[37])*(-1) + (y[11]*y[12]*y[19]*p[33])*(-1) + (y[11]*y[19]*y[9]*p[39])*(-1);
                ydot[12] = y[15]*y[19]*y[5]*p[32] + (y[11]*y[12]*y[19]*p[33])*(-1);
                ydot[13] = y[21]*y[22]*y[23]*p[24] + (y[13]*y[14]*y[22]*p[25])*(-1);
                ydot[14] = y[20]*y[21]*y[22]*p[22] + y[21]*y[22]*y[23]*p[24] + y[21]*y[22]*y[24]*p[26] + y[21]*y[22]*y[25]*p[28] + y[21]*y[22]*y[26]*p[30] + (y[13]*y[14]*y[22]*p[25])*(-1) + (y[14]*y[2]*y[22]*p[23])*(-1) + (y[14]*y[22]*y[6]*p[27])*(-1) + (y[14]*y[22]*y[7]*p[29])*(-1) + (y[14]*y[22]*y[8]*p[31])*(-1);
                ydot[15] = y[10]*y[11]*y[19]*p[37] + y[11]*y[12]*y[19]*p[33] + y[11]*y[19]*y[9]*p[39] + (y[15]*y[19]*y[5]*p[32])*(-1) + (y[15]*y[19]*y[6]*p[36])*(-1) + (y[15]*y[19]*y[7]*p[38])*(-1);
                ydot[16] = y[0]*y[17]*y[3]*p[20] + (y[16]*y[17]*y[4]*p[21])*(-1);
                ydot[17] = 0;
                ydot[18] = 0;
                ydot[19] = 0;
                ydot[20] = y[14]*y[2]*y[22]*p[23] + (y[20]*y[21]*y[22]*p[22])*(-1);
                ydot[21] = y[13]*y[14]*y[22]*p[25] + y[14]*y[2]*y[22]*p[23] + y[14]*y[22]*y[6]*p[27] + y[14]*y[22]*y[7]*p[29] + y[14]*y[22]*y[8]*p[31] + (y[20]*y[21]*y[22]*p[22])*(-1) + (y[21]*y[22]*y[23]*p[24])*(-1) + (y[21]*y[22]*y[24]*p[26])*(-1) + (y[21]*y[22]*y[25]*p[28])*(-1) + (y[21]*y[22]*y[26]*p[30])*(-1);
                ydot[22] = 0;
                ydot[23] = y[13]*y[14]*y[22]*p[25] + (y[21]*y[22]*y[23]*p[24])*(-1);
                ydot[24] = y[14]*y[22]*y[6]*p[27] + (y[21]*y[22]*y[24]*p[26])*(-1);
                ydot[25] = y[14]*y[22]*y[7]*p[29] + (y[21]*y[22]*y[25]*p[28])*(-1);
                ydot[26] = y[14]*y[22]*y[8]*p[31] + (y[21]*y[22]*y[26]*p[30])*(-1);
                ''', ['ydot', 't', 'y', 'p'])
            return ydot
        
    else:
        
        def ode_rhs(self, t, y, p):
            ydot = self.ydot
            ydot[0] = y[16]*y[17]*y[4]*p[21] + (y[0]*y[17]*y[3]*p[20])*(-1)
            ydot[1] = y[19]*y[2]*p[34] + (y[1]*y[19]*p[35])*(-1)
            ydot[2] = y[1]*y[19]*p[35] + y[20]*y[21]*y[22]*p[22] + (y[19]*y[2]*p[34])*(-1) + (y[14]*y[2]*y[22]*p[23])*(-1)
            ydot[3] = y[16]*y[17]*y[4]*p[21] + (y[0]*y[17]*y[3]*p[20])*(-1)
            ydot[4] = y[0]*y[17]*y[3]*p[20] + (y[16]*y[17]*y[4]*p[21])*(-1)
            ydot[5] = y[11]*y[12]*y[19]*p[33] + (y[15]*y[19]*y[5]*p[32])*(-1)
            ydot[6] = y[10]*y[11]*y[19]*p[37] + y[21]*y[22]*y[24]*p[26] + (y[14]*y[22]*y[6]*p[27])*(-1) + (y[15]*y[19]*y[6]*p[36])*(-1)
            ydot[7] = y[11]*y[19]*y[9]*p[39] + y[21]*y[22]*y[25]*p[28] + (y[14]*y[22]*y[7]*p[29])*(-1) + (y[15]*y[19]*y[7]*p[38])*(-1)
            ydot[8] = y[21]*y[22]*y[26]*p[30] + (y[14]*y[22]*y[8]*p[31])*(-1)
            ydot[9] = y[15]*y[19]*y[7]*p[38] + (y[11]*y[19]*y[9]*p[39])*(-1)
            ydot[10] = y[15]*y[19]*y[6]*p[36] + (y[10]*y[11]*y[19]*p[37])*(-1)
            ydot[11] = y[15]*y[19]*y[5]*p[32] + y[15]*y[19]*y[6]*p[36] + y[15]*y[19]*y[7]*p[38] + (y[10]*y[11]*y[19]*p[37])*(-1) + (y[11]*y[12]*y[19]*p[33])*(-1) + (y[11]*y[19]*y[9]*p[39])*(-1)
            ydot[12] = y[15]*y[19]*y[5]*p[32] + (y[11]*y[12]*y[19]*p[33])*(-1)
            ydot[13] = y[21]*y[22]*y[23]*p[24] + (y[13]*y[14]*y[22]*p[25])*(-1)
            ydot[14] = y[20]*y[21]*y[22]*p[22] + y[21]*y[22]*y[23]*p[24] + y[21]*y[22]*y[24]*p[26] + y[21]*y[22]*y[25]*p[28] + y[21]*y[22]*y[26]*p[30] + (y[13]*y[14]*y[22]*p[25])*(-1) + (y[14]*y[2]*y[22]*p[23])*(-1) + (y[14]*y[22]*y[6]*p[27])*(-1) + (y[14]*y[22]*y[7]*p[29])*(-1) + (y[14]*y[22]*y[8]*p[31])*(-1)
            ydot[15] = y[10]*y[11]*y[19]*p[37] + y[11]*y[12]*y[19]*p[33] + y[11]*y[19]*y[9]*p[39] + (y[15]*y[19]*y[5]*p[32])*(-1) + (y[15]*y[19]*y[6]*p[36])*(-1) + (y[15]*y[19]*y[7]*p[38])*(-1)
            ydot[16] = y[0]*y[17]*y[3]*p[20] + (y[16]*y[17]*y[4]*p[21])*(-1)
            ydot[17] = 0
            ydot[18] = 0
            ydot[19] = 0
            ydot[20] = y[14]*y[2]*y[22]*p[23] + (y[20]*y[21]*y[22]*p[22])*(-1)
            ydot[21] = y[13]*y[14]*y[22]*p[25] + y[14]*y[2]*y[22]*p[23] + y[14]*y[22]*y[6]*p[27] + y[14]*y[22]*y[7]*p[29] + y[14]*y[22]*y[8]*p[31] + (y[20]*y[21]*y[22]*p[22])*(-1) + (y[21]*y[22]*y[23]*p[24])*(-1) + (y[21]*y[22]*y[24]*p[26])*(-1) + (y[21]*y[22]*y[25]*p[28])*(-1) + (y[21]*y[22]*y[26]*p[30])*(-1)
            ydot[22] = 0
            ydot[23] = y[13]*y[14]*y[22]*p[25] + (y[21]*y[22]*y[23]*p[24])*(-1)
            ydot[24] = y[14]*y[22]*y[6]*p[27] + (y[21]*y[22]*y[24]*p[26])*(-1)
            ydot[25] = y[14]*y[22]*y[7]*p[29] + (y[21]*y[22]*y[25]*p[28])*(-1)
            ydot[26] = y[14]*y[22]*y[8]*p[31] + (y[21]*y[22]*y[26]*p[30])*(-1)
            return ydot
        
    
    def simulate(self, tspan, param_values=None, view=False):
        if param_values is not None:
            # accept vector of parameter values as an argument
            if len(param_values) != len(self.parameters):
                raise Exception("param_values must have length %d" %
                                len(self.parameters))
            self.sim_param_values[:] = param_values
        else:
            # create parameter vector from the values in the model
            self.sim_param_values[:] = [p.value for p in self.parameters]
        self.y0.fill(0)
        for ic in self.initials:
            self.y0[ic.species_index] = self.sim_param_values[ic.param_index]
        if self.y is None or len(tspan) != len(self.y):
            self.y = numpy.empty((len(tspan), len(self.y0)))
            if len(self.observables):
                self.yobs = numpy.ndarray(len(tspan),
                                list(zip((obs.name for obs in self.observables),
                                    itertools.repeat(float))))
            else:
                self.yobs = numpy.ndarray((len(tspan), 0))
            self.yobs_view = self.yobs.view(float).reshape(len(self.yobs),
                                                           -1)
        # perform the actual integration
        self.integrator.set_initial_value(self.y0, tspan[0])
        self.integrator.set_f_params(self.sim_param_values)
        self.y[0] = self.y0
        t = 1
        while self.integrator.successful() and self.integrator.t < tspan[-1]:
            self.y[t] = self.integrator.integrate(tspan[t])
            t += 1
        for i, obs in enumerate(self.observables):
            self.yobs_view[:, i] = \
                (self.y[:, obs.species] * obs.coefficients).sum(1)
        if view:
            y_out = self.y.view()
            yobs_out = self.yobs.view()
            for a in y_out, yobs_out:
                a.flags.writeable = False
        else:
            y_out = self.y.copy()
            yobs_out = self.yobs.copy()
        return (y_out, yobs_out)
    
