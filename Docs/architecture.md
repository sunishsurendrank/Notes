# Architectural Things

## Modeling notations 

- ArchiMate
- CSDM
- BPMN


## Designs

- 𝗦𝘁𝗮𝘁𝗶𝗰 𝗖𝗼𝗻𝘁𝗲𝗻𝘁 𝗛𝗼𝘀𝘁𝗶𝗻𝗴: used to optimise webpage loading time. It stores static content (information that doesn't change often, like an author's bio or an MP3 file) - separately from dynamic content (like stock prices).

- 𝗣𝗲𝗲𝗿-𝘁𝗼-𝗣𝗲𝗲𝗿: Involves multiple components called Peers, where a pear may function both as a client, requesting services from other peers, and as a server, providing services to other peers.

- 𝗣𝘂𝗯𝗹𝗶𝘀𝗵𝗲𝗿-𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗿: Used to send (publishes) relevant messages to places that have subscribed to a topic.

- 𝗦𝗵𝗮𝗿𝗱𝗶𝗻𝗴 𝗣𝗮𝘁𝘁𝗲𝗿𝗻 – Used to partition data in a database to speed commands or queries.

- 𝗖𝗶𝗿𝗰𝘂𝗶𝘁 𝗕𝗿𝗲𝗮𝗸𝗲𝗿: Helps make systems more fault tolerant by minimising the effects of a hazard by rerouting traffic to another service.

- 𝗟𝗮𝘆𝗲𝗿𝗲𝗱 𝗣𝗮𝘁𝘁𝗲𝗿𝗻: Generally used to develop applications that include groups of subtasks that execute in a specific order.

- 𝗖𝗹𝗶𝗲𝗻𝘁-𝗦𝗲𝗿𝘃𝗲𝗿: A peer-to-peer architecture that is comprised of a client, which requests a service, and a server, which provides the service.

- 𝗠𝗮𝘀𝘁𝗲𝗿-𝗦𝗹𝗮𝘃𝗲: Consists of two components; the master distributes the work among identical slaves and computes a final result from the results which the slaves return.

- 𝗣𝗶𝗽𝗲-𝗙𝗶𝗹𝘁𝗲𝗿: Used to structure systems that produce and process a stream of data.

- 𝗘𝘃𝗲𝗻𝘁-𝗗𝗿𝗶𝘃𝗲𝗻: Uses events to trigger and communicate between decoupled services.

- 𝗠𝗼𝗱𝗲𝗹-𝗩𝗶𝗲𝘄-𝗖𝗼𝗻𝘁𝗿𝗼𝗹𝗹𝗲𝗿: Divides an application into three components. The model contains the application's data and main functionality; the view displays data and interacts with the user; and the controller handles user input and acts as the mediator between the model and the view.

- 𝗧𝗵𝗿𝗼𝘁𝘁𝗹𝗶𝗻𝗴 - pattern controls how fast data flows into a target. It's often used to prevent failure during a distributed denial of service attack or to manage cloud infrastructure costs.

- 𝗠𝗶𝗰𝗿𝗼𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀: Used to create multiple services that work interdependently to create a larger application.

- 𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗤𝘂𝗲𝗿𝘆 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗶𝗯𝗶𝗹𝗶𝘁𝘆 𝗦𝗲𝗴𝗿𝗲𝗴𝗮𝘁𝗶𝗼𝗻: Used to separate read and write activities to provide greater stability, scalability, and performance.