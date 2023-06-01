<h2 id="rect">Exercises</h2>
<h4> Text Analysis </h4>
You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class
'analysedText' with the following methods -

<ul>
    <li> Constructor (__init__) - This method should take the argument <code>text</code>, make it lower case, and remove all punctuation.  Assume only the following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?). Assign this newly formatted text to a new attribute called <code>fmtText</code>.
    <li> freqAll - This method should create and <strong>return</strong> dictionary of all unique words in the text, along with the number of times they occur in the text. Each key in the dictionary should be the unique word appearing in the text and the associated value should be the number of times it occurs in the text. Create this dictionary from the <code>fmtText</code> attribute.
    <li> freqOf - This method should take a word as an argument and <strong>return</strong> the number of occurrences of that word in <code>fmtText</code>.
</ul>
 The skeleton code has been given to you. Docstrings can be ignored for the purpose of the exercise. <br>
 <i> Hint: Some useful functions are <code>replace()</code>, <code>lower()</code>, <code>split()</code>, <code>count()</code> </i><br>
