---
layout: post
title: Understanding Callbacks in Javascript
---

<h1>Understanding Callbacks in Javascript</h1>

While first starting with javascript, one of the most difficult concepts for me was callbacks. Undoubtedly there are others out there who share a similar confusion, and hopefully I can help clear some of it up.

Say we have a function get(), which retrieves a value based on a key that you pass to it.  It also returns a callback when the value is retrieved.

{% highlight javascript %}
get(key, function(value) {
	console.log(value);
});

{% endhighlight %}

In the example above, you pass the key to get() as the first parameter, the second is an anonymous function that will be called once the operation is complete.  Now lets look at a definition of get().

{% highlight javascript %}
var get = function(key, callback) {
	value = getValue(key);
	return callback(value);
}

{% endhighlight %}

To break this down.
