
# 1. IAM - Identity Access Management
- IAM Policy
- IAM Role (Through which the Services communicate internally)
- IAM Security Tools
    - Credential Report
    - Access Advisor
# 2.  EC2 Instance
- Connection to EC2 Instance
   - Session Manager
   - SSH
   - EC2 Instant Connect

- EC2 instance flavours
  - c -compute series
  - r -With larger ram series
  - t - normal series

- Purchase Option
  - on-Demand
  - Reservered Instance
  - Savings Plan
  - Spot Instance
  - Dedicated Host
  - Dedicated Instance
  - Capacity Reservation

- AMI - Amazone Machine Image
  - User can build custom images using EC2 Image Builder

# 3. Storage

### EBS Volumes (Elastic Block Storage)
 - We pay for I/O and Incremental Storage 

###  EFS (Elastic File System)
- Multiple machines can access

### Amazon FSX - Windows File System

### EC2 Instance Store - High Perfromance

# 4. Amazon S3
- Maximum 5GB item upload at a time
- Class
  - Standard
  - Standard - IA(Infrequent Access)
  - One Zone - IA(Infrequent Access)
  - Glacier Instant Retrieval
  - Glacier Flexible Retrival
  - Glacier Deep Archive
  - Intelligent Tiering
### S3 transfer Acceleration

# 5. ELB (Elastics Load Balancer)
- L7 - Application LB
- L4 - Network LB
- L3 - Gateway LB

### AutoScaling (User create ASG (auto scaling group))
- Manualy
- Automatic (Simple, Target, Scheduled Autoscaling)
- Predective



# 6. Databases
  - RDB -Postgres, Microsoft SQL, Oracle
  - DynamoDB -nosql DB
  - Redshift - For Data anatlyics and data warehouse
  - Amazon EMR - it helps Hadoop Cluster
  - Document DB
  - Amazon Netptune - graph DB
  - Amazone QLDB - Ledger

# 7. Computing Service
### ECS
### Fargate
### Lambda 
- First 1 million request free)
### AWS Batch 
- Its is like Lambda but difference is it will spin up the EC2 instance at backend)

# 8. Global Application
### Route53
- Create DNS Record and routing
  - Simple Routing
  - Weighted Routing
  - Latency Routing
  - Failover Routing
### CloudFront
- Content delivery network
- It caches content neart location of the user

# 9. Virtaul Private Cloud
- Subnet to Subnet communication happens via Routing Table
- VPC Peering - Connect two VPC
- Transit GateWay - Connect many VPC together
- VPC EndPoints
- Direct Connect - private cable connection between on premsis and cloud
- AWS Private Link
- Site-Site VPN

# 10. Operations
 - CloudFormation
 - AWSOpswork - (Chef, Puppet)
 - BeanStack
 - CodeDeploy
 - Code Commit - Code Guru - Code Build - Code Pipeline - Code Artifactory
 - Code star

 # 11. Cloud Monitoring
 - Cloud Watch
 - Cloud Trail
 - AWS xray - to scan api calls
 - Amazon SNS - Simple Notification Service

# 12. Queue Service
- Simple Queue Service
- Amazon Kinesis
- Amazon MQ

# 13. Machine learning

- Rekoginition
- Transcribe
- Polly
- Translate
- Amazon lex
- Amazon connect
- Sagemaker
- Amazon Forcast
- Personalize
- Kendra (ML powered search engine)
- Textract

# 14. Security
 - AWS Sheild - Protect from DDOS Attack
 - AWS WAf - Project from SQL Injection
 - AWS Config

 # 15. Billing
 - Price calculator
 - Cost and Usage Report
 - Cost Explorer
 - Budget
 - Trusted Advisor
  
# General Things

![image](/images/aws/scope.png)






