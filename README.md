<a name="prawvents"></a>
# PRAWvents, Events for PRAW
A simple wrapper to write event-based bots with [PRAW](https://praw.readthedocs.io/en/latest).

## Scope
You can register event handlers for everything thats based on the praw [stream_generator](https://praw.readthedocs.io/en/latest/code_overview/other/util.html#praw.models.util.stream_generator)
Any other functionality is offered as-is, since this subclasses the main PRAW [Reddit](https://praw.readthedocs.io/en/latest/code_overview/reddit_instance.html) instance.

A async version of this should be possible, but is not yet planned.

# Quickstart

This is a simple bot that will print out the subreddit and the submission title for all posts in the subreddits AskReddit and pics, while skipping the existing posts in AskReddit.
This example assumes the presence of a [praw.ini](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html) in your working directory.
```py
from prawvents import EventReddit
from praw import reddit

r = EventReddit(user_agent=f"ExampleBot for prawvents version (0.0.1) by /u/laundmo") # change the description and username!

sub1 = r.subreddit("AskReddit")
sub2 = r.subreddit("pics")

def handle_exception(e): # very dumb exception handler
    print(e)

@r.register_event(sub1.stream.submissions, err_handler=handle_exception, skip_existing=True)
@r.register_event(sub2.stream.submissions, err_handler=handle_exception)
def handle(submission: reddit.Submission):
    print(submission.subreddit, submission.title)

r.run_loop()
```

# Docs
<a name="prawvents.RedditEventDecorator"></a>
## RedditEventDecorator Objects

```python
class RedditEventDecorator()
```

Decorator class for event handlers.

<a name="prawvents.RedditEventDecorator.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(reddit: praw.Reddit, stream: RStream, err_handler: Callable)
```

Initialise RedditEventDecorator.

**Arguments**:

- `reddit` _EventReddit_ - The `EventReddit` instance
- `stream` _RStream_ - The stream to which the event responds.
- `err_handler` _Callable_ - A function thats called with the exception as a argument.

<a name="prawvents.RedditEventDecorator.__call__"></a>
#### \_\_call\_\_

```python
 | __call__(f: Callable) -> Callable
```

Set the event handler.

**Arguments**:

- `f` _Callable_ - The event handler function.


**Returns**:

- `Callable` - The function.

<a name="prawvents.EventReddit"></a>
## EventReddit Objects

```python
class EventReddit(praw.Reddit)
```

Main Reddit instance, subclass of [praw.Reddit](https://praw.readthedocs.io/en/latest/code_overview/reddit_instance.html).

**Arguments**:

- `praw` _praw.Reddit_ - Praw Reddit superclass.

<a name="prawvents.EventReddit.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(*args, **kwargs)
```

Initialise EventReddit. All arguments are passed through to [praw.Reddit](https://praw.readthedocs.io/en/latest/code_overview/reddit_instance.html)

<a name="prawvents.EventReddit.register_event"></a>
#### register\_event

```python
 | register_event(stream: RStream, err_handler: Callable = None, **kwargs) -> RedditEventDecorator
```

Register a event, should generally be used as a decorator like this:

```py
@r.register_event(subreddit.stream.submissions, err_handler=handle_exception)
def event_handler(submission):
    pass
```

**Arguments**:

- `stream` _RStream_ - The stream to which the event responds.
- `err_handler` _Callable, optional_ - The error handler for this event. Defaults to None.


**Returns**:

- `RedditEventDecorator` - The decorator instance.

<a name="prawvents.EventReddit.handle_exception"></a>
#### handle\_exception

```python
 | handle_exception(f: Callable, e: Exception)
```

Handle a Exception happening in a function f

**Arguments**:

- `f` _Callable_ - The function which threw the exception.
- `e` _Exception_ - The exception which was thrown.


**Raises**:

- `e` - The Exception that was thrown.

<a name="prawvents.EventReddit.run_stream_till_none"></a>
#### run\_stream\_till\_none

```python
 | run_stream_till_none(stream: RStream, funcs: Iterable[Callable]) -> None
```

Runs a stream until none is returned

**Arguments**:

- `stream` _RStream_ - The finalized stream to run.
- `funcs` _Iterable[Callable]_ - The functions which handle this stream.

<a name="prawvents.EventReddit.run_loop"></a>
#### run\_loop

```python
 | run_loop(interweave=True) -> None
```

Run the event loop. If interweave is Truthy, events from multiple streams will be mixed to ensure a single high-traffic stream cant take up the entire event loop. This is highly 
recommended.

**Arguments**:

- `interweave` _bool, optional_ - Whether to interweave streams to ensure fair distribution. Defaults to True.