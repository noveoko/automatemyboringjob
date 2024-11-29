# Real-time Motion Amplification on Mobile Devices

This repository contains an open-source implementation of a real-time motion amplification algorithm suitable for mobile devices, including smartphones. The algorithm is based on motion enhancement by moving average differencing (MEMAD), a temporal high-pass filter for video streams. MEMAD can amplify small moving objects or subtle motion in larger objects and is computationally simple enough to be implemented in real time on smartphones.

## Abstract

A simple motion amplification algorithm suitable for real-time applications on mobile devices, including smartphones, is presented. It is based on motion enhancement by moving average differencing (MEMAD), a temporal high-pass filter for video streams. MEMAD can amplify small moving objects or subtle motion in larger objects. It is computationally sufficiently simple to be implemented in real time on smartphones. In the specific implementation as an Android phone app, MEMAD is demonstrated on examples chosen such as to motivate applications in the engineering, biological, and medical sciences.

## Keywords

Motion amplification, Mobile applications, Telehealth, MRI, Imaging

## Introduction

Motion amplification is a fascinating tool that can make unperceivable motion visible by computational amplification. Many motion amplification algorithms are based on principles that have been developed decades ago but really gained traction more recently with the improvement of computational power. This development also enabled more accurate and powerful motion amplification algorithms including motion microscopy.

It would be interesting to evaluate whether motion amplification is possible in real time on mobile devices such as smartphones. Real-time applications of motion amplification, i.e., with instantaneous results and without any processing on other equipment than the smartphone itself, could be beneficial whenever an instant exploration of motion is desired. For example, in remote biological field studies, for pulse measurement in communication apps, or in on-site diagnostics of machinery. To approach this goal, this research took a step back from the previously mentioned state-of-the-art algorithms, thereby developing a computationally simple motion amplification algorithm that is less demanding on processing hardware and thus suitable for real-time smartphone apps.

## Methods
