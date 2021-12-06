// =============================================================================
// PROJECT CHRONO - http://projectchrono.org
//
// Copyright (c) 2014 projectchrono.org
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be found
// in the LICENSE file at the top level of the distribution and at
// http://projectchrono.org/license-chrono.txt.
//
// =============================================================================
// Authors: Radu Serban
// =============================================================================
//
// Chrono configuration header file
//
// Automatically created during CMake configuration.
//
// =============================================================================

#ifndef CH_CONFIG_H
#define CH_CONFIG_H

// -----------------------------------------------------------------------------
// Macros specifying enabled Chrono modules
// -----------------------------------------------------------------------------

// If module CASCADE was enabled, define CHRONO_CASCADE
#undef CHRONO_CASCADE

// If module COSIMULATION was enabled, define CHRONO_COSIMULATION
#undef CHRONO_COSIMULATION

// If module IRRLICHT was enabled, define CHRONO_IRRLICHT
#undef CHRONO_IRRLICHT

// If module MATLAB was enabled, define CHRONO_MATLAB
#undef CHRONO_MATLAB

// If module PARDISO_MKL was enabled, define CHRONO_PARDISO_MKL
#undef CHRONO_PARDISO_MKL

// If module MUMPS was enabled, define CHRONO_MUMPS
#undef CHRONO_MUMPS

// If module OPENGL was enabled, define CHRONO_OPENGL
#undef CHRONO_OPENGL

// If module MULTICORE was enabled, define CHRONO_MULTICORE
#undef CHRONO_MULTICORE

// If module POSTPROCESS was enabled, define CHRONO_POSTPROCESS
#undef CHRONO_POSTPROCESS

// If module PYTHON was enabled, define CHRONO_PYTHON
#undef CHRONO_PYTHON

// If module VEHICLE was enabled, define CHRONO_VEHICLE
#undef CHRONO_VEHICLE

// If module FSI was enabled, define CHRONO_FSI
#undef CHRONO_FSI

// If module GPU was enabled, define CHRONO_GPU
#undef CHRONO_GPU

// If module SYNCHRONO was enabled, define CHRONO_SYNCHRONO
#undef CHRONO_SYNCHRONO

// If module SENSOR was enabled, define CHRONO_SENSOR
#undef CHRONO_SENSOR

// If module PARDISOPROJECT was enabled, define CHRONO_PARDISOPROJECT
#undef CHRONO_PARDISOPROJECT

// -----------------------------------------------------------------------------
// OpenMP settings
// -----------------------------------------------------------------------------

// If OpenMP is found the following define is set
//   #define CHRONO_OMP_FOUND
// Set the highest OpenMP version supported, one of:
//   #define CHRONO_OMP_VERSION "2.0"
//   #define CHRONO_OMP_VERSION "3.0"
//   #define CHRONO_OMP_VERSION "4.0"
// and define one or more of the following, as appropriate
//   #define CHRONO_OMP_20
//   #define CHRONO_OMP_30
//   #define CHRONO_OMP_40






// If OpenMP support was enabled in the main ChronoEngine library, define CHRONO_OPENMP_ENABLED
#undef CHRONO_OPENMP_ENABLED

// If TBB support was enabled in the main ChronoEngine library, define CHRONO_TBB_ENABLED
#undef CHRONO_TBB_ENABLED

// -----------------------------------------------------------------------------
// SSE settings
// -----------------------------------------------------------------------------

// If SSE support was found, then
//   #define CHRONO_HAS_SSE
// and set the SSE level support, one of the following
//   #define CHRONO_SSE_LEVEL "1.0"
//   #define CHRONO_SSE_LEVEL "2.0"
//   #define CHRONO_SSE_LEVEL "3.0"
//   #define CHRONO_SSE_LEVEL "4.1"
//   #define CHRONO_SSE_LEVEL "4.2"
// and define one or more of the following, as appropriate
//   #define CHRONO_SSE_1.0
//   #define CHRONO_SSE_2.0
//   #define CHRONO_SSE_3.0
//   #define CHRONO_SSE_4.1
//   #define CHRONO_SSE_4.2









// -----------------------------------------------------------------------------

// If AVX support was found, then
//   #define CHRONO_HAS_AVX
// and set the SSE level support, one of the following
//   #define CHRONO_AVX_LEVEL "1.0"
//   #define CHRONO_AVX_LEVEL "2.0"
// and define one or more of the following, as appropriate
//   #define CHRONO_AVX_1.0
//   #define CHRONO_AVX_2.0






// -----------------------------------------------------------------------------

// If NEON support was found, then
//   #define CHRONO_HAS_NEON

#define CHRONO_HAS_NEON

// -----------------------------------------------------------------------------

// If FMA support was found, then
//   #define CHRONO_HAS_FMA



// -----------------------------------------------------------------------------

// If HDF5 was found, then
//   #define CHRONO_HAS_HDF5



// -----------------------------------------------------------------------------
// CUDA settings
// -----------------------------------------------------------------------------

// If CUDA is available, define CHRONO_CUDA_FOUND and CHRONO_CUDA_VERSION

#undef CHRONO_CUDA_FOUND
#undef CHRONO_CUDA_VERSION

// -----------------------------------------------------------------------------

// If Google Test and Benchmark are enabled and available, then
//   #define CHRONO_HAS_GTEST
//   #define CHRONO_HAS_GBENCHMARK




#endif