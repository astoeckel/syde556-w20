/*
 *  Cinder -- C++ Single Spiking Neuron Simulator
 *  Copyright (C) 2015, 2016  Andreas Stöckel, Christoph Jenzen
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <iostream>

#include <cinder/cinder.hpp>

using namespace cinder;

/**
 * A current source which injects a constant current during a given interval.
 */
class RampCurrentSource
    : public CurrentSourceBase<StepCurrentSourceState,
                               StepCurrentSourceParameters> {
private:
	Time m_t_start;
	Time m_t_end;

public:
	using Base =
	    CurrentSourceBase<StepCurrentSourceState, StepCurrentSourceParameters>;
	using Base::p;
	using Base::Base;

	RampCurrentSource(Current step_current, RealTime t_start,
	                  RealTime t_end = RealTime(std::numeric_limits<Real>::max()))
	    : Base({{step_current, t_start, t_end}})
	{
	}

	/**
	 * Converts the floating point times from the parameters to the internal
	 * fixed point times.
	 */
	template <typename State2, typename System>
	void init(Time, const State2 &, const System &)
	{
		m_t_start = Time::sec(p().t_start());
		m_t_end = Time::sec(p().t_end());
	}

	/**
	 * Returns the position of the next discontinuity in the differential
	 * equation.
	 */
	Time next_discontinuity(Time t) const
	{
		return (t < m_t_start ? m_t_start : (t < m_t_end ? m_t_end : MAX_TIME));
	}

	/**
	 * Emit a spike whenever the threshold potential is surpassed.
	 */
	template <typename State, typename System>
	void update(Time t, State &s, System &sys)
	{
		const double phase = (t - m_t_start).sec() / (m_t_end - m_t_start).sec();
		if (phase < 0.0) {
			s[0] = 0.0;
		} else if (phase <= 1.0) {
			s[0] = phase * p().i_offset();
		} else {
			s[0] = 0.0;
		}
	}
};

int main()
{
	// Use the DormandPrince integrator with default target error
	DormandPrinceIntegrator integrator;

	// Record the neuron state as CSV to cout
	CSVRecorder recorder(std::cout);

	// Use the AutoController class to automatically abort the simulation
	// once the neuron has settled to its resting state
	AutoController controller;

	// Assemble the neuron (an Izhikevich neuron with default parameters)
//	auto current_source = StepCurrentSource(0.02_nA, 1_s, 1.2_s);
//	auto current_source = StepCurrentSource(0.025_nA, 1_s, 1.2_s);
	auto current_source = RampCurrentSource(0.1_nA, 0.6_s, 5_s);

	auto neuron = make_neuron<HodgkinHuxley>(current_source);

	// Simulate the resulting ODE -- the recorder will record the results
	auto solver = make_solver(neuron, integrator, recorder, controller);
	solver.solve(2_s);
//	solver.solve(5_s);
}
