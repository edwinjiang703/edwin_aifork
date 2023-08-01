HSBC DBaaS Delivery Content
Resource Tiering Self-Service Portal
❖ Application classification based on service level and importance:
❖ Definition of resource pools in the self-service portal with 8 types available
❖ Creation of database instances that comply with HSBC Global standards
PLATINUM: RAC with 2 DG
❖ Implementation or expansion of existing HSBC Global database service scripts
GOLD: RAC with 1 DG
Includes single instance to RAC conversion, DG setup, RAC One Node
SILVER: RAC One Node with 1 DG
Creation, PDB plug/unplug operations, etc.
Resource Pool Definition Resource Pool Capabilities
❖ Construction of different resource pools for different purposes
❖ Rapid provisioning of resources to significantly shorten delivery process (UAT environment)
ZHJ, IFC, NHC production resource pools OEM DBaaS platform
❖ Dynamic resource adjustment for online scaling up or down
NHC UAT resource pool
Service Catalog Utilization of PDB migration feature to enable quick deployment across different resource pools
❖ Resource and performance definition for databases of different application tiers
Self-Service Portal
❖ Monitoring of Exadata hardware and DBaaS resource pools through OEM
Requirement: A temporary pattern definition for Phase 1
Resource Pool Functionality and Alerts; Customized dashboard for quick information overview
CPUs: 2
SGA: 12G; PGA: 4G; Sessions: 900
Disaster Recovery Planning Service Expansion
❖ Coexistence of PDBs with different character sets within a single CDB
❖ RAC and RAC One Node:
❖ Expanded existing Global scripts for DB Service functionality
Primary: ZHJ -> Standby: IFC, NHC Three Data Centers in Two Locations
Role-based mode
Primary: ZHJ -> Standby: IFC Application isolation mode: preferred and available
Primary: ZHJ -> Standby: NHC Standby in read-only mode
Primary: IFC -> Standby: NHC ❖ LDAP-based login
Primary: IFC -> Standby: ZHJ
Copyright © 2021 Oracle and/or its affiliates.
1

| [] | [] | [] |
| --- | --- | --- |


