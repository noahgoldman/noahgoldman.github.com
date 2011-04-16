---
layout: post
title: Understanding Callbacks in Javascript
---

<h1>Understanding Callbacks in Javascript</h1>

While first starting with javascript, one of the most difficult concepts for me was callbacks. Undoubtedly there are others out there who share a similar confusion, and hopefully I can help clear some of it up.

Say we have a function get(), which retrieves a value based on a key that you pass to it.  It also returns a callback when the value is retrieved.

{% highlight javascript linenos %}
get(key, function(value) {
	console.log(value);
});
{% endhighlight %}

In the example above, you pass the key to get() as the first parameter, the second is an anonymous function that will be called once the operation is complete.  Now lets look at a definition of get().

{% highlight javascript linenos %}
var get = function(key, callback) {
	value = getValue(key);
	return callback(value);
}
{% endhighlight %}

To break this down:
1. Assign the variable get to an anonymous function.
2. Get the value of the key. The value is retrieved, and once that operation is complete, it continues on.
3. Call the callback function that was passed to the get() function with the second parameter.  The important thing to realize about this action is that get() will call the specific function that you passed to it, and it will only call it once the get() function has finished.  The return statement is not necessary, but it is known to be good practice in node.js ([See here](http://stella.laurenzo.org/2011/03/bulletproof-node-js-coding/)).

The most important thing to understand is that the get() function calls the function that you pass to it, like in the first example.  When the get() function calls the callback, its calling the anonymous function that you gave to it.

I hope that this summary helps someone understand this concept.  Its certainly a difficult idea to wrap your head around coming from another background.
