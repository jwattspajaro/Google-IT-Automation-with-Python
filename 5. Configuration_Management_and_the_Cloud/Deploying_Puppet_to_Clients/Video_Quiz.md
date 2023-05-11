
### Puppet Nodes
Pregunta

#### In Puppet, what can we use to categorize in order to apply different rules to different systems?



⚫  **Node definitions**


⚪ Manifest file


⚪ Array configuration


⚪ Template

✅ Correcto
Nice job! Different kinds of nodes are defined, allowing different sets of rule catalogs to apply to different types of machines.

----
### Puppet's Certificate Infrastructure
Pregunta

#### What is the purpose of the Certificate Authority (CA)?


⚪ To test rules in the manifest


⚪ To manage templates


⚫ To validate the identity of each machine	


⚪ To handle push/pull requests

✅ Correcto
### Awesome! The CA either queues a certificate request for manual validation, or uses pre-shared data to verify before sending the certificate to the agent.

---
### Setting up Puppet Clients and Servers
Pregunta

### What kind of security encryption is used when the Puppet Certificate Authority validates the identity of a node?


⚫ Secure Sockets Layer (SSL)


⚪ Secure Shell (SSH)


⚪ Pretty Good Privacy (PGP)


⚪ Transport Layer Security (TLS)

✅ Correcto
Great work! The Certificate Authority creates an SSL key for the agent machine and creates a certificate request.

----
### Modifying and Testing Manifests
What does the puppet parser validate command do?


⚫ Checks the syntax of the manifest.


⚪ Runs full No Operations simulations.


⚪ Tests automatically using facts we set to evaluate the resulting catalog.


Forcibly applies manifests locally.

✅Correcto
Great work! The puppet parser validate command checks the syntax of the manifest to make sure it's correct.

