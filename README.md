A Python distributed tasking system based on *etcd*.

## Why another tasking system?

I've been a long-time Celery user, and the author of the Qpid transport for Kombu which allows
Celery to run on the Qpid message broker. In the Python community Celery is the most commonly used
project, and it is really great, but it has several challenges that make it very difficult for Pulp
to use.

* The typical message broker install is a single point of failure, and clustering them isn't always
easy or reliable. *etcd* is very easy to cluster because its self-organizing.

* The typical message broker has limited capacity because unless its clustered, you can't add more
hardware resources to the system. *etcd* is easy to run on lots of hardware and scale the resources
it has.

* There have been many deadlock concerns around Celery's fork safety requirements. `cabbage`
does no forking so it's not a concern.

* Celery, Kombu, and Billiard code is very complicated. Contributing back to Celery is challenging.
The core folks are very helpful, but the code does very advanced things, so it's practically
difficult to attract contributors. We want something really simple.

* Celery protects against task code segfaulting, but its forking and interprocess communication code
is complicated. Cabbage expects an external process launcher to relaunch any workers as necessary.
`cabbage` delegates a lot of responsibility to other tools like `systemd`, `supervisord`,
`kubernetes`, etc.

* Pulp has to build its own safety mechanisms on top of Celery to ensure tasks that edit certain
types of data cannot run at the same time as other tasks that also edit that type of data. It would
be great to build this into the tasking system itself.

* Celery uses kernel facilities directly such as `epoll` or `kpoll`. This is efficient, but it
creates practical challenges when another reactor technology, e.g. Proton Reactor, needs tobe used
with it. `cabbage` uses an asyncio based etcd driver to efficiently interact with the nearest etcd
node.

## Design

`cabbage` uses asyncio to provide concurrency. Each task itself is a co-routine that should yield
control at some point using the `async` and `await` syntax.

Run `cabbage` using the `cabbage` Python entry point.


## Install

tasking_prototype depends on syntax changes introduced in Python 3.5. You can install it from PyPI
with the following command::

    $ pip install cabbage


## License

Copyright Brian Bouterse License, and licensed under the GPLv3 license. See the LICENSE file for
details.
