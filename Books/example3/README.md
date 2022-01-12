# EXAMPLE3 : Site Reliability Engineering - How google runs productions systems

Site Reliability Engineering - How google runs productions systems
Betsy Beyer, Chris Jones, Jennifer Petoff & Niall Murphy

https://sre.google/sre-book/table-of-contents/

https://sre.google/sre-book/bibliography/#Bur06

## Daily - tier 1
- https://sre.google/sre-book/service-level-objectives/
    - SLO, logarithmic scale, percentile
    - Standarize Indicators
    - Perfection can wait
- https://sre.google/sre-book/eliminating-toil/
    - Toil defined
    - Why Less Toil Is Better
- https://sre.google/sre-book/monitoring-distributed-systems/
    - Definitions
    - Symptoms Versus Causes
    - ACLs
- https://sre.google/sre-book/automation-at-google/
    - python
- https://sre.google/sre-book/release-engineering/
    - The Role of a Release Engineer
    - Canary testing
        - https://www.usenix.org/system/files/login/articles/05_mcnutt.pdf
        - https://www.optimizely.com/optimization-glossary/canary-testing/
    - Hermetic Builds
        - https://dl.acm.org/doi/10.1145/2854146
        - https://www.youtube.com/watch?v=W71BTkUbdqE
    - Continuous Build and Deployment
        - Rapid
        - Bazel
            - https://bazel.build/faq.html
    - Sisyphus
- https://sre.google/sre-book/simplicity/
    - Simplicity
    - The price of reliability is the pursuit of the utmost simplicity.
    - The Virtue of Boring
    - I Won’t Give Up My Code!!
        - https://www.sec.gov/litigation/admin/2013/34-70694.pdf
    - Minimal APIs
- https://sre.google/sre-book/practical-alerting/
    - The Rise of Borgmon
        - https://research.google/pubs/pub43438/
        - https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43438.pdf
    - Time-Series Monitoring Outside of Google
    - Riemann, Heka, Bosun, and Prometheus
        - https://prometheus.io/
            - https://prometheus.io/docs/introduction/overview/
    - Storage in the Time-Series Arena
    - Sharding the Monitoring Topology
- https://sre.google/sre-book/being-on-call/
    - Being On-Call
    - Feeling Safe
    - A Treacherous Enemy: Operational Underload
- https://sre.google/sre-book/effective-troubleshooting/
    - Shakespeare Has a Problem
    - App engine
- https://sre.google/sre-book/emergency-response/
    - Test-Induced Emergency
    - Process-Induced Emergency
    - All Problems Have Solutions
- https://sre.google/sre-book/managing-incidents/
    - ad hoc incident management practice
    - You would sympathize, but doing so would require cognitive effort that you are holding in reserve for your job.
    - make irrelevant but hard-to-refute comments
    - Elements of Incident Management Process
- https://sre.google/sre-book/postmortem-culture/
    - Best Practice: Avoid Blame and Keep It Constructive
    - Introducing a Postmortem Culture
- https://sre.google/sre-book/tracking-outages/
    - Escalator, Outalator
- https://sre.google/sre-book/testing-reliability/
    - Testing for Reliability
    - If you haven't tried it, assume it's broken.
    - Types of Software Testing
- https://sre.google/sre-book/software-engineering-in-sre/
    - Software Engineering in SRE
    - Our Solution: Intent-Based Capacity Planning
    - Intent-Based Capacity Planning
    - Designing at the right level
- https://sre.google/sre-book/load-balancing-frontend/
    - Load Balancing at the Frontend
    - Power Isn’t the Answer
    - Load Balancing Using DNS
    - Load Balancing at the Virtual IP Address
    - ? 9 ceros
- https://sre.google/sre-book/load-balancing-datacenter/
    - Load Balancing in the Datacenter
    - Identifying Bad Tasks: Flow Control and Lame Ducks
    - Load Balancing Policies
    - ? good
- https://sre.google/sre-book/handling-overload/
    - Handling Overload
    - The Pitfalls of "Queries per Second"
    - Client request rejection probability
    - ? good
    - Handling Overload Errors
- https://sre.google/sre-book/addressing-cascading-failures/

## More information - tier 2

- https://sre.google/sre-book/bibliography/#All10
    - https://www.oreilly.com/library/view/web-operations/9781449377465/
    - > Vída util, picos de trafico