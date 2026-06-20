# AWS Automated Cost Optimizer

## Overview
This project automatically stops running EC2 instances using AWS Lambda and EventBridge Scheduler to reduce AWS costs.

## Services Used
- AWS Lambda
- Amazon EC2
- Amazon EventBridge
- IAM
- CloudWatch

## Architecture

EventBridge Scheduler
        ↓
      Lambda
        ↓
    Describe EC2
        ↓
 Stop Running Instances

## Features
- Automatic EC2 shutdown
- Cost optimization
- Serverless automation
- Scheduled execution

## Author
Priyanka Mandve