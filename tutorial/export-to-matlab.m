
classdef atlas_rbm_construct_model_from_metabolic_network
    % 
    % A class implementing the ordinary differential equations
    % for the atlas_rbm_construct_model_from_metabolic_network model.
    %
    % Save as atlas_rbm_construct_model_from_metabolic_network.m.
    %
    % Generated by pysb.export.matlab.MatlabExporter.
    %
    % Properties
    % ----------
    % observables : struct
    %     A struct containing the names of the observables from the
    %     PySB model as field names. Each field in the struct
    %     maps the observable name to a matrix with two rows:
    %     the first row specifies the indices of the species
    %     associated with the observable, and the second row
    %     specifies the coefficients associated with the species.
    %     For any given timecourse of model species resulting from
    %     integration, the timecourse for an observable can be
    %     retrieved using the get_observable method, described
    %     below.
    %
    % parameters : struct
    %     A struct containing the names of the parameters from the
    %     PySB model as field names. The nominal values are set by
    %     the constructor and their values can be overriden
    %     explicitly once an instance has been created.
    %
    % Methods
    % -------
    % atlas_rbm_construct_model_from_metabolic_network.odes(tspan, y0)
    %     The right-hand side function for the ODEs of the model,
    %     for use with MATLAB ODE solvers (see Examples).
    %
    % atlas_rbm_construct_model_from_metabolic_network.get_initial_values()
    %     Returns a vector of initial values for all species,
    %     specified in the order that they occur in the original
    %     PySB model (i.e., in the order found in model.species).
    %     Non-zero initial conditions are specified using the
    %     named parameters included as properties of the instance.
    %     Hence initial conditions other than the defaults can be
    %     used by assigning a value to the named parameter and then
    %     calling this method. The vector returned by the method
    %     is used for integration by passing it to the MATLAB
    %     solver as the y0 argument.
    %
    % atlas_rbm_construct_model_from_metabolic_network.get_observables(y)
    %     Given a matrix of timecourses for all model species
    %     (i.e., resulting from an integration of the model),
    %     get the trajectories corresponding to the observables.
    %     Timecourses are returned as a struct which can be
    %     indexed by observable name.
    %
    % Examples
    % --------
    % Example integration using default initial and parameter
    % values:
    %
    % >> m = atlas_rbm_construct_model_from_metabolic_network();
    % >> tspan = [0 100];
    % >> [t y] = ode15s(@m.odes, tspan, m.get_initial_values());
    %
    % Retrieving the observables:
    %
    % >> y_obs = m.get_observables(y)
    %
    properties
        observables
        parameters
    end

    methods
        function self = atlas_rbm_construct_model_from_metabolic_network()
            % Assign default parameter values
            self.parameters = struct( ...
                't0_met_ACETYL_COA_cyt', 0, ...
                't0_met_ALLOLACTOSE_cyt', 0, ...
                't0_met_Alpha_lactose_cyt', 0, ...
                't0_met_Beta_D_Galactosides_cyt', 0, ...
                't0_met_CO_A_cyt', 0, ...
                't0_met_CPD_15972_cyt', 0, ...
                't0_met_CPD_3561_cyt', 0, ...
                't0_met_CPD_3785_cyt', 0, ...
                't0_met_CPD_3801_cyt', 0, ...
                't0_met_D_ARABINOSE_cyt', 0, ...
                't0_met_Fructofuranose_cyt', 0, ...
                't0_met_GALACTOSE_cyt', 0, ...
                't0_met_Glucopyranose_cyt', 0, ...
                't0_met_MELIBIOSE_cyt', 0, ...
                't0_met_PROTON_cyt', 0, ...
                't0_met_WATER_cyt', 100, ...
                't0_met__6_Acetyl_Beta_D_Galactosides_cyt', 0, ...
                't0_prot_lacA_cyt', 0, ...
                't0_prot_lacY_cyt', 0, ...
                't0_prot_lacZ_cyt', 1, ...
                'fwd_GALACTOACETYLTRAN_RXN', 1, ...
                'rvs_GALACTOACETYLTRAN_RXN', 0, ...
                'fwd_TRANS_RXN_24', 1, ...
                'rvs_TRANS_RXN_24', 0, ...
                'fwd_TRANS_RXN_94', 1, ...
                'rvs_TRANS_RXN_94', 0, ...
                'fwd_RXN0_7215', 1, ...
                'rvs_RXN0_7215', 0, ...
                'fwd_RXN0_7217', 1, ...
                'rvs_RXN0_7217', 0, ...
                'fwd_RXN_17755', 1, ...
                'rvs_RXN_17755', 0, ...
                'fwd_BETAGALACTOSID_RXN', 1, ...
                'rvs_BETAGALACTOSID_RXN', 0, ...
                'fwd_RXN0_5363', 1, ...
                'rvs_RXN0_5363', 1, ...
                'fwd_RXN_17726', 1, ...
                'rvs_RXN_17726', 0, ...
                'fwd_RXN0_7219', 1, ...
                'rvs_RXN0_7219', 0, ...
                't0_dna_Alpha_lactose_per', 100, ...
                't0_dna_PROTON_per', 100, ...
                't0_prot_lacY_imem', 1);

            % Define species indices (first row) and coefficients
            % (second row) of named observables
            self.observables = struct( ...
                'obs_met_ACETYL_COA_cyt', [1; 1], ...
                'obs_met_ALLOLACTOSE_cyt', [2; 1], ...
                'obs_met_Alpha_lactose_cyt', [3; 1], ...
                'obs_met_Beta_D_Galactosides_cyt', [4; 1], ...
                'obs_met_CO_A_cyt', [5; 1], ...
                'obs_met_CPD_15972_cyt', [6; 1], ...
                'obs_met_CPD_3561_cyt', [7; 1], ...
                'obs_met_CPD_3785_cyt', [8; 1], ...
                'obs_met_CPD_3801_cyt', [9; 1], ...
                'obs_met_D_ARABINOSE_cyt', [10; 1], ...
                'obs_met_Fructofuranose_cyt', [11; 1], ...
                'obs_met_GALACTOSE_cyt', [12; 1], ...
                'obs_met_Glucopyranose_cyt', [13; 1], ...
                'obs_met_MELIBIOSE_cyt', [14; 1], ...
                'obs_met_PROTON_cyt', [15; 1], ...
                'obs_met_WATER_cyt', [16; 1], ...
                'obs_met__6_Acetyl_Beta_D_Galactosides_cyt', [17; 1], ...
                'obs_met_Alpha_lactose_per', [21; 1], ...
                'obs_met_PROTON_per', [22; 1], ...
                'obs_prot_lacY_imem', [23; 1]);
        end

        function initial_values = get_initial_values(self)
            % Return the vector of initial conditions for all
            % species based on the values of the parameters
            % as currently defined in the instance.

            initial_values = zeros(1,27);
            initial_values(1) = self.parameters.t0_met_ACETYL_COA_cyt; % met(name='ACETYL_COA', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(2) = self.parameters.t0_met_ALLOLACTOSE_cyt; % met(name='ALLOLACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(3) = self.parameters.t0_met_Alpha_lactose_cyt; % met(name='Alpha_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(4) = self.parameters.t0_met_Beta_D_Galactosides_cyt; % met(name='Beta_D_Galactosides', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(5) = self.parameters.t0_met_CO_A_cyt; % met(name='CO_A', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(6) = self.parameters.t0_met_CPD_15972_cyt; % met(name='CPD_15972', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(7) = self.parameters.t0_met_CPD_3561_cyt; % met(name='CPD_3561', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(8) = self.parameters.t0_met_CPD_3785_cyt; % met(name='CPD_3785', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(9) = self.parameters.t0_met_CPD_3801_cyt; % met(name='CPD_3801', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(10) = self.parameters.t0_met_D_ARABINOSE_cyt; % met(name='D_ARABINOSE', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(11) = self.parameters.t0_met_Fructofuranose_cyt; % met(name='Fructofuranose', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(12) = self.parameters.t0_met_GALACTOSE_cyt; % met(name='GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(13) = self.parameters.t0_met_Glucopyranose_cyt; % met(name='Glucopyranose', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(14) = self.parameters.t0_met_MELIBIOSE_cyt; % met(name='MELIBIOSE', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(15) = self.parameters.t0_met_PROTON_cyt; % met(name='PROTON', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(16) = self.parameters.t0_met_WATER_cyt; % met(name='WATER', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(17) = self.parameters.t0_met__6_Acetyl_Beta_D_Galactosides_cyt; % met(name='_6_Acetyl_Beta_D_Galactosides', loc='cyt', dna=None, met=None, prot=None, rna=None)
            initial_values(18) = self.parameters.t0_prot_lacA_cyt; % prot(name='lacA', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=None)
            initial_values(19) = self.parameters.t0_prot_lacY_cyt; % prot(name='lacY', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=None)
            initial_values(20) = self.parameters.t0_prot_lacZ_cyt; % prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=None)
            initial_values(21) = self.parameters.t0_dna_Alpha_lactose_per; % met(name='Alpha_lactose', loc='per', dna=None, met=None, prot=None, rna=None)
            initial_values(22) = self.parameters.t0_dna_PROTON_per; % met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None)
            initial_values(23) = self.parameters.t0_prot_lacY_imem; % prot(name='lacY', loc='imem', dna=None, met=None, prot=None, rna=None, up=None, dw=None)
        end

        function y = odes(self, tspan, y0)
            % Right hand side function for the ODEs

            % Shorthand for the struct of model parameters
            p = self.parameters;

            % met(name='ACETYL_COA', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(1,1) = y0(17)*y0(18)*y0(5)*p.rvs_GALACTOACETYLTRAN_RXN + (y0(1)*y0(18)*y0(4)*p.fwd_GALACTOACETYLTRAN_RXN)*(-1);
            % met(name='ALLOLACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(2,1) = y0(20)*y0(3)*p.fwd_RXN0_5363 + (y0(2)*y0(20)*p.rvs_RXN0_5363)*(-1);
            % met(name='Alpha_lactose', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(3,1) = y0(2)*y0(20)*p.rvs_RXN0_5363 + y0(21)*y0(22)*y0(23)*p.fwd_TRANS_RXN_24 + (y0(20)*y0(3)*p.fwd_RXN0_5363)*(-1) + (y0(15)*y0(3)*y0(23)*p.rvs_TRANS_RXN_24)*(-1);
            % met(name='Beta_D_Galactosides', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(4,1) = y0(17)*y0(18)*y0(5)*p.rvs_GALACTOACETYLTRAN_RXN + (y0(1)*y0(18)*y0(4)*p.fwd_GALACTOACETYLTRAN_RXN)*(-1);
            % met(name='CO_A', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(5,1) = y0(1)*y0(18)*y0(4)*p.fwd_GALACTOACETYLTRAN_RXN + (y0(17)*y0(18)*y0(5)*p.rvs_GALACTOACETYLTRAN_RXN)*(-1);
            % met(name='CPD_15972', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(6,1) = y0(12)*y0(13)*y0(20)*p.rvs_BETAGALACTOSID_RXN + (y0(16)*y0(20)*y0(6)*p.fwd_BETAGALACTOSID_RXN)*(-1);
            % met(name='CPD_3561', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(7,1) = y0(11)*y0(12)*y0(20)*p.rvs_RXN_17726 + y0(22)*y0(23)*y0(25)*p.fwd_RXN0_7215 + (y0(15)*y0(23)*y0(7)*p.rvs_RXN0_7215)*(-1) + (y0(16)*y0(20)*y0(7)*p.fwd_RXN_17726)*(-1);
            % met(name='CPD_3785', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(8,1) = y0(12)*y0(20)*y0(10)*p.rvs_RXN0_7219 + y0(22)*y0(23)*y0(26)*p.fwd_RXN0_7217 + (y0(15)*y0(23)*y0(8)*p.rvs_RXN0_7217)*(-1) + (y0(16)*y0(20)*y0(8)*p.fwd_RXN0_7219)*(-1);
            % met(name='CPD_3801', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(9,1) = y0(22)*y0(23)*y0(27)*p.fwd_RXN_17755 + (y0(15)*y0(23)*y0(9)*p.rvs_RXN_17755)*(-1);
            % met(name='D_ARABINOSE', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(10,1) = y0(16)*y0(20)*y0(8)*p.fwd_RXN0_7219 + (y0(12)*y0(20)*y0(10)*p.rvs_RXN0_7219)*(-1);
            % met(name='Fructofuranose', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(11,1) = y0(16)*y0(20)*y0(7)*p.fwd_RXN_17726 + (y0(11)*y0(12)*y0(20)*p.rvs_RXN_17726)*(-1);
            % met(name='GALACTOSE', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(12,1) = y0(16)*y0(20)*y0(6)*p.fwd_BETAGALACTOSID_RXN + y0(16)*y0(20)*y0(7)*p.fwd_RXN_17726 + y0(16)*y0(20)*y0(8)*p.fwd_RXN0_7219 + (y0(11)*y0(12)*y0(20)*p.rvs_RXN_17726)*(-1) + (y0(12)*y0(13)*y0(20)*p.rvs_BETAGALACTOSID_RXN)*(-1) + (y0(12)*y0(20)*y0(10)*p.rvs_RXN0_7219)*(-1);
            % met(name='Glucopyranose', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(13,1) = y0(16)*y0(20)*y0(6)*p.fwd_BETAGALACTOSID_RXN + (y0(12)*y0(13)*y0(20)*p.rvs_BETAGALACTOSID_RXN)*(-1);
            % met(name='MELIBIOSE', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(14,1) = y0(22)*y0(23)*y0(24)*p.fwd_TRANS_RXN_94 + (y0(14)*y0(15)*y0(23)*p.rvs_TRANS_RXN_94)*(-1);
            % met(name='PROTON', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(15,1) = y0(21)*y0(22)*y0(23)*p.fwd_TRANS_RXN_24 + y0(22)*y0(23)*y0(24)*p.fwd_TRANS_RXN_94 + y0(22)*y0(23)*y0(25)*p.fwd_RXN0_7215 + y0(22)*y0(23)*y0(26)*p.fwd_RXN0_7217 + y0(22)*y0(23)*y0(27)*p.fwd_RXN_17755 + (y0(14)*y0(15)*y0(23)*p.rvs_TRANS_RXN_94)*(-1) + (y0(15)*y0(3)*y0(23)*p.rvs_TRANS_RXN_24)*(-1) + (y0(15)*y0(23)*y0(7)*p.rvs_RXN0_7215)*(-1) + (y0(15)*y0(23)*y0(8)*p.rvs_RXN0_7217)*(-1) + (y0(15)*y0(23)*y0(9)*p.rvs_RXN_17755)*(-1);
            % met(name='WATER', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(16,1) = y0(11)*y0(12)*y0(20)*p.rvs_RXN_17726 + y0(12)*y0(13)*y0(20)*p.rvs_BETAGALACTOSID_RXN + y0(12)*y0(20)*y0(10)*p.rvs_RXN0_7219 + (y0(16)*y0(20)*y0(6)*p.fwd_BETAGALACTOSID_RXN)*(-1) + (y0(16)*y0(20)*y0(7)*p.fwd_RXN_17726)*(-1) + (y0(16)*y0(20)*y0(8)*p.fwd_RXN0_7219)*(-1);
            % met(name='_6_Acetyl_Beta_D_Galactosides', loc='cyt', dna=None, met=None, prot=None, rna=None);
            y(17,1) = y0(1)*y0(18)*y0(4)*p.fwd_GALACTOACETYLTRAN_RXN + (y0(17)*y0(18)*y0(5)*p.rvs_GALACTOACETYLTRAN_RXN)*(-1);
            % prot(name='lacA', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=None);
            y(18,1) = 0;
            % prot(name='lacY', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=None);
            y(19,1) = 0;
            % prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=None);
            y(20,1) = 0;
            % met(name='Alpha_lactose', loc='per', dna=None, met=None, prot=None, rna=None);
            y(21,1) = y0(15)*y0(3)*y0(23)*p.rvs_TRANS_RXN_24 + (y0(21)*y0(22)*y0(23)*p.fwd_TRANS_RXN_24)*(-1);
            % met(name='PROTON', loc='per', dna=None, met=None, prot=None, rna=None);
            y(22,1) = y0(14)*y0(15)*y0(23)*p.rvs_TRANS_RXN_94 + y0(15)*y0(3)*y0(23)*p.rvs_TRANS_RXN_24 + y0(15)*y0(23)*y0(7)*p.rvs_RXN0_7215 + y0(15)*y0(23)*y0(8)*p.rvs_RXN0_7217 + y0(15)*y0(23)*y0(9)*p.rvs_RXN_17755 + (y0(21)*y0(22)*y0(23)*p.fwd_TRANS_RXN_24)*(-1) + (y0(22)*y0(23)*y0(24)*p.fwd_TRANS_RXN_94)*(-1) + (y0(22)*y0(23)*y0(25)*p.fwd_RXN0_7215)*(-1) + (y0(22)*y0(23)*y0(26)*p.fwd_RXN0_7217)*(-1) + (y0(22)*y0(23)*y0(27)*p.fwd_RXN_17755)*(-1);
            % prot(name='lacY', loc='imem', dna=None, met=None, prot=None, rna=None, up=None, dw=None);
            y(23,1) = 0;
            % met(name='MELIBIOSE', loc='per', dna=None, met=None, prot=None, rna=None);
            y(24,1) = y0(14)*y0(15)*y0(23)*p.rvs_TRANS_RXN_94 + (y0(22)*y0(23)*y0(24)*p.fwd_TRANS_RXN_94)*(-1);
            % met(name='CPD_3561', loc='per', dna=None, met=None, prot=None, rna=None);
            y(25,1) = y0(15)*y0(23)*y0(7)*p.rvs_RXN0_7215 + (y0(22)*y0(23)*y0(25)*p.fwd_RXN0_7215)*(-1);
            % met(name='CPD_3785', loc='per', dna=None, met=None, prot=None, rna=None);
            y(26,1) = y0(15)*y0(23)*y0(8)*p.rvs_RXN0_7217 + (y0(22)*y0(23)*y0(26)*p.fwd_RXN0_7217)*(-1);
            % met(name='CPD_3801', loc='per', dna=None, met=None, prot=None, rna=None);
            y(27,1) = y0(15)*y0(23)*y0(9)*p.rvs_RXN_17755 + (y0(22)*y0(23)*y0(27)*p.fwd_RXN_17755)*(-1);
        end

        function y_obs = get_observables(self, y)
            % Retrieve the trajectories for the model observables
            % from a matrix of the trajectories of all model
            % species.

            % Initialize the struct of observable timecourses
            % that we will return
            y_obs = struct();

            % Iterate over the observables;
            observable_names = fieldnames(self.observables);
            for i = 1:numel(observable_names)
                obs_matrix = self.observables.(observable_names{i});
                if isempty(obs_matrix)
                    y_obs.(observable_names{i}) = zeros(size(y, 1), 1);
                    continue
                end
                species = obs_matrix(1, :);
                coefficients = obs_matrix(2, :);
                y_obs.(observable_names{i}) = ...
                                y(:, species) * coefficients';
            end
        end
    end
end
