#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

import numpy as np
import simulation


class SimulationConstantEnvironment(TestCase):

    def setUp(self):
        self.ε = np.zeros(1000, dtype=int)

    def test_default_pop(self):
        π = simulation.simulation(1000, 200, 0.1, 0, 2.0, 0.2, 0.5, self.ε)

        assert np.allclose(π[-1, :], 1), np.unique(π[-1, :])

    def test_η_0(self):
        # this won't work with isogenic - totally up to selection here
        π = simulation.simulation(1000, 200, 0, 0, 2.0, 0.2, 0.5, self.ε)

        assert np.allclose(π[-1, :], 1), np.unique(π[-1, :])

    def test_isogenic_pop(self):
        def isogenic(N):
            x = np.ones(N) * 0.5
            return x

        π = simulation.simulation(1000, 200, 0.1, 0, 2.0, 0.2, isogenic, self.ε)

        assert np.allclose(π[-1, :], 1), np.unique(π[-1, :])


    def test_isogenic_pop_η_0(self):
        def isogenic(N):
            x = np.ones(N) * 0.5
            return x

        π = simulation.simulation(1000, 200, 0, 0, 2.0, 0.2, isogenic, self.ε)

        assert np.allclose(π[-1, :], 0.5), np.unique(π[-1, :])


class DeterministicConstantEnvironment(TestCase):

    def setUp(self):
        self.ε = np.zeros(1000, dtype=int)

    def test_isogenic_pop_η_0_s_0(self):
        π, f = simulation.deterministic(1000, 100, 0, 0, 1, 0, 0.5, self.ϵ)

        assert np.allclose(π[-1], 0.5), np.unique(π[-1])

    def test_isogenic_pop_η_0(self):
        π, f = simulation.deterministic(1000, 200, 0.1, 0, 1, 0, 0.5, self.ϵ)

        assert np.allclose(π[-1], 1), np.unique(π[-1])

    def test_uniform_pop_η_0(self):
        π, f = simulation.deterministic(1000, 200, 0.1, 0, 1, 0, lambda: simulation.uniform(10), self.ϵ)

        assert np.allclose(π[-1], 1), np.unique(π[-1])