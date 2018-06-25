# Lab3_starter_code

COMPSCI 677 Distributed and Operating Systems

Spring 2018

Programming Assignment 3: Asterix and the Olympic Games (Fault Tolerant edition)

Due: 11:55pm, April 23, 2018

    You may work in groups of two for this lab assignment.

    This project has two purposes: to familiarize you with concepts in caching and fault tolerance

    You can be creative with this project. You should implement the lab in python but are free to use any abstractions such as sockets, RPCs, RMIs, threads, events, etc. that might be needed. You can also build on the code that you wrote for the previous lab.

A: The problem

    After the tremendous success of the winter Olympic games, the Gauls are preparing for the summer Olympic games. The summer games are expected to be singificantly more popular and draw more traffic than the winter games.
    Part 1: Caching and Cache Consistency
    The Gauls are continuing their effort to prepare for the expected surge in the number of smart stones accessing sports information. Both performance and reliability enhancements are planned. Previously the front-end stone server was replicated but each request still needed to access a backend database, which resulted in slow disk I/Os To enhance performance, Obelix has decided to add a cache to each front-end server. The cache stores a copy of recently accessed scores for each sport. When a tablet makes a request to the stone server, the front-end server first checks the cache to see if the requested data is cached. In the event of a cache hit, the cached data is used to service the request. Since the cache is a memory cache, cache hits avoid the need for disk I/O at the database server and reduce latency. However, if the request results in a cache miss, the front-end servers must request data from the backend server like before. Like before Cacofonix sends sports score updates to the stone server. Since the scores are frequently updated, cache consistency is a must. The Gauls do not like their fish or their sports scores to be stale! To serve fresh up-to-date scores, Obelix has decided to implement two approaches to cache consistency: push-based consistency and pull-based consistency. In push-based consistency, each front-end server tracks what scores are cached within its local cache. Upon receiving an update, it sends this update to the backend server and sends cache invalidate messages to caches at other front-end servers that cache this score. Cache invalidate messages cause the cache to remove the corresponding item from the cache and a subsequent request causes a cache miss and the item is brought back into the cache. In pull-based consistency, it is responsibility of the cache to periodically poll the front-end server to check if the data has changed. If data is unchanged, it remains in the cache, otherwise the stale data is removed. The frequency at which the caches poll the server determines the degree of freshness. You are free to implement any approach to determine the poll frequency---the frequency can be fixed or determined based on popularity (more popular sports see more frequent polls).

    Your system needs to support both push and pull-based techniques. However when the system starts up, you need to provide a configuration option that specifies which of the two should be used.
    Part 2: Fault Tolerance
    To ensure reliability, the front-end servers must be able to handle failures. In this lab, only crash failures of the front end need to be handled. Assume that one of the front end servers can fail at any point. Implement heartbeat messages to detect the presence of a failure and have the remaining front end take over the tasks of the failed server. This may involve (i) informing the Cacofonix server to send subsequent updates to the new server (if needed), (ii) informing clients to send subequent requests to the new server (you can assume that clients register themselves with the Stone server at startup and hence the servers know all clients accessing the server). Your code must be able to handle the crash failure of either front-end server. Further, your code must be able to handle recovery -- when the crashed server comes back up, it should be able to resume operation by taking over its original responsibilities (e.g., roughly half the clients are reassigned to the server and if the server was receiving updates previously, it should do so again). Like before, assume that the front end servers not only receive requests for scores but one of them also receives score updates from the Cacofonix process and then sends an update to the database tier. Further, while the API exposed by front-end servers is identical to labs 1 and 2. You may make suitable modifications to the interface for tasks related to client registrations, caching and fault tolerance. as well as design any internal interface between the caches, the front-end and back-end processes for this purpose (you can deisgn it any way you wish and this interface should be documented in your README file).

    Like before assume that there are N tablets, each of which is a client, that needs to be periodically updated with sports scores. (N should be configurable in your system).

    Like before, Cacofonix, the village bard, is responsible for providing Obelix's server live updates from the olympic stadium, which he does by singing the scores and thereby sending updated scores to one of the front-end servers.
    Optional Extra Credit Part:
    This part is optional and may be attempted for extra credit. This part can take significant effort and you should attempt it only if the rest of your lab is complete and in good shape. Consider a system with four front-end servers and a single database server. Assume that the village is infiltrated with a Roman spy who may corrupt one of the servers by hacking into them and causing them to fail in a Byzantine fashion (i.e., failed servers no longer crash, they can see Byzantine faults).

    Assume that the servers implement consensus using Paxos or RAFT in this sytem to avoid problems. Also, assume that there are 4 front-end replicas and that each request is sent to all of them and the replicas run Paxos to reach agreement on the answer or run RAFT to each agreement on the order of requests before providing a reply to a request. How might such a system work? Explain clearly how the Paxos or RAFT algorithm can be used by your front-end servers and you would have implemented it in your current design. Do not blindly cut and paste the algorithm from the class slides or from the Internet - you are expected to gain some faimiliarity with it and come up with a design that uses Paxos or RAFT. Provide a writeup of your design with the main design document. You can pick either Paxos or RAFT for this part - there is no need to do both.

    Finally, implement your Paxos or RAFT design in the front-end nodes and conduct a simple experiment to demonstrate it works (e.g., the system functions even when nodes fail or one of the node produces an incorrent answer).
    Requirements:
        You need to implement BOTH Part 1 and Part 2. The extra credit part is optional.
        All the requirements of Project 2 still apply to Project 1, except that you no longer needs vector clocks or clock syncronization. 
    Other requirements:

        No GUIs are required. Simple command line interfaces and textual output of scores and medal tallies are fine.

        You are free to develop your solution on any platform, but please ensure that your programs compile and run on the edlab machines (See note below). 

B. Performance Evaluation and Measurement

    Compute the average response time of your new server as before for different number of clients and request rates. Comment on the performance improvements, if any, observed due to caching.
    Design tests to compare pull and push-based consistency. Make observations on much stale data is observed in pull-based consistency in your design.
    Design test to show the reliability of your system when a front-end server fails. Demonstrate that recovery can also be performed.

    Make necessary plots to support your conclusions.

C. What you will submit
When you have finished implementing the complete assignment as described above, you will submit your solution in github. Do not treat gihub as a final submission site where you only submit the final submission. You must use github for code development throughout the lab. Check in your code, test cases, documentation regularly as you work on the lab. We will look at your check-in history, number of commits, comments on your commits, etc., and assign points for proper use of github (see grading policy below).
Each program must work correctly and be documented. The final submission on githiub should contain:

    A README file listing the names of students in your group (do not include student IDs) as well as how to run your code. If we can't run it, we can't grade it. The REAMDE file should be a simple "user manual" of how to setup and run your code on the ed-lab.
    source code in the src directory for all three parts, with in-line comments.
    An electronic copy of the output generated by running your program. Print informative messages when a client or server receives and sends key messages and the scores/medal tallies.
    A seperate design document of approximately three pages describing the overall program design, a description of "how it works", and design tradeoffs considered and made. Be sure to document the design of EACH part separately. Also describe possible improvements and extensions to your program (and sketch how they might be made).
    A seperate description of the tests you ran on your program to convince yourself that it is indeed correct. Also describe any cases for which your program is known not to work correctly.
    Performance results.

D. Grading policy for all programming assignments

        Program Listing
            works correctly ------------- 60% (30% for each of the two parts)
            in-line comments / documentation -------- 5% 
        Design Document
            quality of design doc, through description and understandability ------------ 10%
            Creativity of your program design --------- 10% 
        Use of github with checkin comments --- 5%
        Measurement, Performance, Evaluation ---------- 10%
        Grades for late programs will be lowered 12 points per day late.
    Note about edlab machines
    We expect that most of you will work on this lab on your own machine or a machine to which you have access. However we will grade your submission by running it on the EdLab machines, so please keep the following instructions in mind.
    You will soon be given accounts on the EdLab. Read more about edlab and how to access it here
    Although it is not required that you develop your code on the edlab machines, we will run and test your solutions on the edlab machines. Testing your code on the edlab machines is a good way to ensure that we can run and grade your code. Remember, if we can't run it, we can't grade it.
    There are no visiting hours for the edlab. You should all have remote access to the edlab machines. Please make sure you are able to log into and access your edlab accounts.
    IMPORTANT - No submissions are to be made on edlab. Submit your solutions only via github.
    Stumped?
        Who are the Gauls? Read about them on Wikipedia.
        Stumped on how to proceed? Review the comic book Asterix at the Olympic Games from your local library. Better yet, ask the TA or the instructor by posting a question on the Piazza 677 questions. General clarifications are best posted on Piazza. Questions of a personal nature regarding this lab should be asked in person or via email. 
