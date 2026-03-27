# MathWhiz: Serverless AI Agent (AWS Bedrock & Lambda)

## Overview
MathWhiz is an intelligent, serverless AI agent designed to perform complex mathematical operations. It leverages **Amazon Bedrock** for natural language understanding and **AWS Lambda** for secure, backend execution.

## Tech Stack
* **Language:** Python 3.x
* **Cloud Provider:** AWS (Amazon Web Services)
* **AI Orchestration:** Amazon Bedrock Agents
* **Compute:** AWS Lambda (Serverless)
* **API Specification:** OpenAPI (Swagger)

## Architecture
1. **User Input:** Receives math-related queries via the Bedrock Agent.
2. **Reasoning:** Bedrock interprets the intent and identifies the required tool via the OpenAPI schema.
3. **Execution:** The **Lambda function (`lambda_function.py`)** processes the math logic.
4. **Response:** Results are formatted and returned to the user in natural language.

## Key Learnings
* Orchestrated serverless workflows using Action Groups.
* Configured IAM roles for secure cross-service communication.
* Designed modular Python functions for cloud scalability.
