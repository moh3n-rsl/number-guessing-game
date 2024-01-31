# number-guessing-game
Number guessing game in Python

<ul>
<li>Build a Number guessing game, in which the <strong>user selects a range.</strong></li>
<li>Let’s say User selected a range, i.e., from<strong> A </strong>to <strong>B</strong>, where <strong>A</strong> and <strong>B </strong>belong to Integer.</li>
<li>Some <strong>random integer will be selected by the system</strong> and the user has to guess that integer in the <strong>minimum number of guesses</strong></li>
</ul>

<p><strong>Explanation 1</strong>: If the User inputs range, let’s say from 1 to 100. And compiler randomly selected 42 as the integer. And now the guessing game started, so the user entered 50 as his/her <strong>first guess</strong>. The compiler shows “Try Again! You guessed too high”. That’s mean the random number (i.e., 42) doesn’t fall in the range from 50 to 100. That’s the importance of guessing half of the range. And again, the user guesses half of 50 (Could you tell me why?). So the half of 50 is 25. The user enters 25 as his/her <strong>second guess</strong>. This time compiler will show, “Try Again! You guessed too small”. That’s mean the integers less than 25 (from 1 to 25) are useless to be guessed. Now the range for user guessing is shorter, i.e., from 25 to 50. Intelligently! The user guessed half of this range, so that, user guessed 37 as his/her <strong>third guess</strong>. &nbsp;This time again the compiler shows the output, “Try Again! You guessed too small”. For the user, the guessing range is getting smaller by each guess. Now, the guessing range for user is from 37 to 50, for which the user guessed 43 as his/her <strong>fourth guess</strong>. This time the compiler will show an output “Try Again! You guessed too high”. So, the new guessing range for users will be from 37 to 43, again for which the user guessed the half of this range, that is, 40 as his/her <strong>fifth guess</strong>. &nbsp;This time the compiler shows the output, “Try Again! You guessed too small”. Leaving the guess even smaller such that from 41 to 43. And now the user guessed 41 as his/her <strong>sixth guess</strong>. Which is wrong and shows output “Try Again! You guessed too small”. And finally, the User Guessed the right number which is 42 as his/her <strong>seventh guess</strong>.</p>
<p><strong> Total Number of Guesses = 7</strong></p>

<blockquote>
<p>&nbsp;Minimum number of guessing = log<sub>2</sub>(Upper bound – lower bound + 1)</p>
</blockquote>
