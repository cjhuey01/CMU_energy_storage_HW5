from pybamm import exp, tanh, constants, Parameter, ParameterValues


def electrolyte_diffusivity_Nyman2008(c_e, T):
    """
    Diffusivity of LiPF6 in EC:EMC (3:7) as a function of ion concentration. The data
    comes from [1]

    References
    ----------
    .. [1] A. Nyman, M. Behm, and G. Lindbergh, "Electrochemical characterisation and
    modelling of the mass transport phenomena in LiPF6-EC-EMC electrolyte,"
    Electrochim. Acta, vol. 53, no. 22, pp. 6356–6365, 2008.

    Parameters
    ----------
    c_e: :class:`pybamm.Symbol`
        Dimensional electrolyte concentration
    T: :class:`pybamm.Symbol`
        Dimensional temperature

    Returns
    -------
    :class:`pybamm.Symbol`
        Solid diffusivity
    """

    D_c_e = 8.794e-11 * (c_e / 1000) ** 2 - 3.972e-10 * (c_e / 1000) + 4.862e-10

    # Nyman et al. (2008) does not provide temperature dependence

    return D_c_e


def electrolyte_conductivity_Nyman2008(c_e, T):
    """
    Conductivity of LiPF6 in EC:EMC (3:7) as a function of ion concentration. The data
    comes from [1].

    References
    ----------
    .. [1] A. Nyman, M. Behm, and G. Lindbergh, "Electrochemical characterisation and
    modelling of the mass transport phenomena in LiPF6-EC-EMC electrolyte,"
    Electrochim. Acta, vol. 53, no. 22, pp. 6356–6365, 2008.

    Parameters
    ----------
    c_e: :class:`pybamm.Symbol`
        Dimensional electrolyte concentration
    T: :class:`pybamm.Symbol`
        Dimensional temperature

    Returns
    -------
    :class:`pybamm.Symbol`
        Solid diffusivity
    """

    sigma_e = (
        0.1297 * (c_e / 1000) ** 3 - 2.51 * (c_e / 1000) ** 1.5 + 3.329 * (c_e / 1000)
    )

    # Nyman et al. (2008) does not provide temperature dependence

    return sigma_e


def graphite_LGM50_electrolyte_exchange_current_density_Chen2020(c_e, c_s_surf, c_n_max, T):
    """
    Exchange-current density for Butler-Volmer reactions between graphite and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """

    m_ref = 6.48e-7  # (A/m2)(mol/m3)**1.5 - includes ref concentrations
    E_r = 35000
    arrhenius = exp(E_r / constants.R * (1 / 298.15 - 1 / T))

    #c_n_max = Parameter("Maximum concentration in negative electrode [mol.m-3]")

    return (
        m_ref * arrhenius * c_e ** 0.5 * c_s_surf ** 0.5 * (c_n_max - c_s_surf) ** 0.5
    )


def nmc_LGM50_electrolyte_exchange_current_density_Chen2020(c_e, c_s_surf, c_p_max, T):
    """
    Exchange-current density for Butler-Volmer reactions between NMC and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """
    m_ref = 3.42e-6  # (A/m2)(mol/m3)**1.5 - includes ref concentrations
    E_r = 17800
    arrhenius = exp(E_r / constants.R * (1 / 298.15 - 1 / T))

    #c_p_max = Parameter("Maximum concentration in positive electrode [mol.m-3]")

    return (
        m_ref * arrhenius * c_e ** 0.5 * c_s_surf ** 0.5 * (c_p_max - c_s_surf) ** 0.5
    )


def get_parameter_values():
    return ParameterValues(
        {
            "Thermodynamic factor": 1.0,
            "Ambient temperature [K]": 298.15,
            "Cation transference number": 0.2594,
            "Current function [A]": 5.0,
            "Electrode height [m]": 0.065,
            "Electrode width [m]": 1.58,
            "Electrolyte conductivity [S.m-1]": electrolyte_conductivity_Nyman2008,
            "Electrolyte diffusivity [m2.s-1]": electrolyte_diffusivity_Nyman2008,
            "Initial concentration in electrolyte [mol.m-3]": 1000.0,
            "Initial concentration in negative electrode [mol.m-3]": 30170.0,
            "Initial concentration in positive electrode [mol.m-3]": 16653.0,
            "Initial temperature [K]": 298.15,
            "Lower voltage cut-off [V]": 2.5,
            "Maximum concentration in negative electrode [mol.m-3]": 33133.0,
            "Maximum concentration in positive electrode [mol.m-3]": 63104.0,
            "Negative electrode Bruggeman coefficient (electrode)": 1.5,
            "Negative electrode Bruggeman coefficient (electrolyte)": 1.5,
            "Negative electrode OCP entropic change [V.K-1]": 0.0,
            "Negative electrode active material volume fraction": 0.75,
            "Negative electrode conductivity [S.m-1]": 215.0,
            "Negative electrode diffusivity [m2.s-1]": 3.3e-14,
            "Negative electrode electrons in reaction": 1.0,
            "Negative electrode exchange-current density [A.m-2]": graphite_LGM50_electrolyte_exchange_current_density_Chen2020,
            "Negative electrode porosity": 0.25,
            "Negative electrode thickness [m]": 8.52e-05,
            "Negative particle radius [m]": 5.86e-06,
            "Nominal cell capacity [A.h]": 5.0,
            "Number of cells connected in series to make a battery": 1.0,
            "Number of electrodes connected in parallel to make a cell": 1.0,
            "Positive electrode Bruggeman coefficient (electrode)": 1.5,
            "Positive electrode Bruggeman coefficient (electrolyte)": 1.5,
            "Positive electrode OCP entropic change [V.K-1]": 0.0,
            "Positive electrode active material volume fraction": 0.665,
            "Positive electrode conductivity [S.m-1]": 0.18,
            "Positive electrode diffusivity [m2.s-1]": 4e-15,
            "Positive electrode electrons in reaction": 1.0,
            "Positive electrode exchange-current density [A.m-2]": nmc_LGM50_electrolyte_exchange_current_density_Chen2020,
            "Positive electrode porosity": 0.335,
            "Positive electrode thickness [m]": 7.56e-05,
            "Positive particle radius [m]": 5.22e-06,
            "Reference temperature [K]": 298.15,
            "Separator Bruggeman coefficient (electrolyte)": 1.5,
            "Separator porosity": 0.47,
            "Separator thickness [m]": 1.2e-05,
            "Typical current [A]": 5.0,
            "Typical electrolyte concentration [mol.m-3]": 1000.0,
            "Upper voltage cut-off [V]": 4.2,
        }
    )
