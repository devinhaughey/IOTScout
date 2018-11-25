People feel insecure when they lose access to the internet. This becomes life-threatening in case of natural disasters or sudden emergency where local infra is down or they just do not have access to communication with the outside world.
We have proposed a solution that provides people with:
- Ability to send HELP messages to the patrolling vehicles near them (Leveraging the power of vehicles to power the rasp-pi device)
- Report incidents in their surroundings to the authorities responsible
- Generate heat maps to identify the disease affected areas so that government authorities can act upon the initial spread of the disease much more quickly than they usually do.
- Putting a geo-fence around the disease affected area to notify the new visitors of that area with the precautions for the spreading disease.
- Provide an efficient search to find your friends near affected area and know their status 
- A smart search and sort provided to police to never miss the top priority incident
~~~~~~~~~~~~
WE DO THAT USING MQTT, A LIGHTWEIGHT PROTOCOL THAT WORKS WITH LIMITED NETWORK BANDWIDTH USING A VERY SMALL CODE FOOTPRINT.
~~~~~~~~~~~~
IoT SCOUT is a mobile application that users and scouts can install on their phone. By installing the app, the user consents the app to use the following data:
- Location 
- Profile Information
- Date and Time

The user can request immediate help, report diseases/incidents and also check the status of their friends living in an affected area.

The nearby patrolling scout (Police) carries a raspberry pi that continuously listens to the signals from SCOUT APP being sent via MQTT. They receive 2 kinds of signals.
- Emergency Help:

Its a signal when the user presses a red button on the app. This happens when the user needs immediate help. 
- Incident/Disease Report 

This is a signal sent when a user reports an incident like fire, robbery, disease or someone needing help in their surroundings.

Impacts on society :
SAVING LIVES IN DANGER
PREVENTING DISEASE CONTAMINATION
BRINGING AID TO SCOUT'S DAILY OPERATIONS
SMARTER WAYS OF SAFETY MANAGEMENT