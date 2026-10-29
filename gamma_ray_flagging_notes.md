# Gamma-Ray Interval Flagging

## Objective

Practise using Python to pair depth measurements with gamma-ray readings and flag readings above a specified threshold.

## Concepts Applied

- Lists for storing depth and gamma-ray data
- `zip()` for pairing corresponding measurements
- A `for` loop for processing each pair
- `if/else` statements for applying a threshold
- f-strings for formatting output

## Method

The script processes each depth and its corresponding gamma-ray reading. When a reading exceeds 80 API, the interval is flagged for review. Otherwise, the script reports that no flag was triggered by this rule.

## Limitation

The threshold is illustrative and is not a universal criterion for identifying lithology or reservoir intervals. Interpretation requires geological context and other relevant well-log data.

## Key Learning

This exercise demonstrates how basic Python programming can be applied to simple well-log data checks.
