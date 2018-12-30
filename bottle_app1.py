#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file, request
from hashlib import sha256

comment_list = [""]




def create_hash(password):
    pw_bytestring = password.encode()  ## this function was taken: https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
    return sha256(
        pw_bytestring).hexdigest()


def static_file_callback(filename):
    return static_file(filename, root='./')


route('/static/<filename:path>', 'GET', static_file_callback)



def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
        </html>
    """ % (title,text)
    return page






    


def index():
    head = """
                    <link rel="stylesheet" type="text/css" href="./static/mystyle.css" media="screen" />
            <style>
            body {
            background-color:#ffdff1;
            }
            </style>
    """
    body = """
        <IMG SRC="./static/img/drawing-3.svg" align="left" <font width="600" height=200"><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

<h1><font color="purple">
Make-up&Beauty Secrets</font>
</h1>
<ul>
  <li><a href="/">Home</a></li>
  <li><a href="whoarewe">About</a></li>
  <li>  <td><button onclick="location.href='/Comments' " type="button" >COMMENTS</button></td></li>
</ul>



<div class="products">

<h2>Flormar Neon Eye Shadows</h2><br>
<img src="./static/img/img1-1.jpg" alt="Flormar Neon Eye Shadows"width="300" height=200"><br><br>
<p><b>The Flormar Neon Eyeshadow series has attracted my attention with easy to apply and affordable price.<br> We can apply this eyeshadows in the morning quickly and get a healthy and radiant facial appearance.</b></p></div>
<br>
<div class="products">

<h2>Maybelline Lash Senstional Mascara</h2><br>
<img src="./static/img/img4-1.jpg" alt="Maybelline Lash Sensational Mascara" width="300" height=200"><br><br>
<p><b>The Maybelline Lash Sensational Mascara helps add lenght and volume your lashes. It is my favorite.<br> This mascara has an effect all day long. Also, there is no feeling weight on your lashes.</b></p>
</div>



<div class="products">

<h2>Maybelline Fit Me Foundation</h2><br>
<img src="./static/img/img3-1.jpg" alt="Maybelline Fit Me Foundation"width="300" height=200"><br><br>
<p><b>I can say that it's the best foundation i've ever used with a silky texture and matte finish.<br> When you apply in the morning, until the evening your skin doesn't become oily. </b></div>




<div class="products">
<h2>L'Oreal Paris Color Riche x Balmain Lipstick</h2><br>
<img src="./static/img/img5.jpeg" alt="L'Oreal Paris Color Riche Lipstick"width="300" height=200"><br><br>
<p><b>These lipsticks are very easy-to-apply and they are creamy. They are quite lasting so<br> there is no need to refresh during the day. Of course my favorite is "Legend 902" </b></p></div>


<div class="products">
<h2>L'Oreal Paris Micellar Water</h2><br>
<img src="./static/img/img6.jpeg" alt="L'Oreal Paris Micellar Water" width="300" height=200"><br><br>
<p><b>Especially sensitive skin people can use with ease. It definitely doesn't irritate your skin<br> and remove your make-up easily. Also it makes your skin better in regular use.</b>
</p></div>

<div class="products">
<h2>L'Oreal Paris Sugar Scrubs</h2><br>
<img src="./static/img/img7-1.jpg" alt="L'Oreal Paris Sugar Scrubs" width="300" height=200"><br><br>
<p><b>L'Oreal Paris Sugar Scrubs removes dead skin from the skin and provides a smooth skin sensation.<br> Also, in my opinion, Sugar Scrubs is the best idea for black spots on skin.</b>
</p></div>


<div class="products">
<h2>Maybelline Eye Studio Gel Eyeliner</h2><br>
<img src="./static/img/img8-1.jpg" alt="Maybelline Eye Studio Gel Eyeliner"  width="300" height=200"><br><br>
<p><b>This eyeliner is better than its competitors with its implementetion and structure.<br>Even a human who has no dexterity can use it easily. </b>
</p></div>
<a href="https://www.youtube.com/watch?v=a6Mn7PBd2EM">Click Here to View How to Use</a><br>

<br><br>

<h1><font color="purple" face="tahoma">The Favorites of November</h1>
<ol>
<li>L'Oreal Paris Telescopic Carbon Black Mascara</li>
<li>The Balm Matt(e) Hughes Liquid Lipstick
<ol>
<li>Adoring</li>
<li>Charming</li>
</ol>
</li>
<li>Becca Shimmering Skin Perfector Pressed Highlighter</li>
<li>Wet N Wild Rose in the Air </li>
</ol>

<br><br>
<h1>Price Comparison</h1>
	<table>
<tr>
	<th rowspan="2">Products</th>
    <th colspan="3">Store Prices</th>
</tr>
<tr>
	<th>Gratis</th>
	<th>Watsons</th>
	<th>Sephora</th>
</tr>

<tr>
	<td>L'Oreal Paris Telescopic Carbon Black Mascara</td>
	<td>57 TL</td>
	<td>62 TL</td>
	<td>53 TL</td>
</tr>

<tr>
	<td>The Balm Matt(e) Hughes Liquid Lipstick</td>
	<td>47 TL</td>
	<td>93 TL</td>
	<td>87 TL</td>
</tr>
<tr>
<td>Wet N Wild Rose in the Air</td>
<td> - </td>
<td>17 TL</td>
<td>23 TL</td>


</tr>

<tr>
<td>Becca Shimmering Skin Perfector Pressed Highlighter</td>
<td>-</td>
<td>27 TL</td>
<td>32 TL</td>


</tr>


</table>

</font>
        """
    return htmlify(head, body)
route('/', 'GET', index)

def whoarewe():
    head = """
<style>


#About {
     body
     {

		background-color:#ffdff1;

}
	font-size: 27px;
	color:purple;
	text-align:center
</style>

    """
    body = """<h1 id="About">Who Are We?</h1>
<p id="About">Business women are exposed to difficulties
in their private lives as well as the difficulties <br>they experience in their business life.
We help business women with makeup,<br> beauty
and personal care tips, and try to make their lives a little easier.<br>
'cause women have to run the world!</p>
<br><br><br>
<a href="/">Go Home Page</a>
</body>


        """
    return htmlify(head, body)


route('/whoarewe', 'GET', whoarewe)


password = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"



def commentspage():
    commentspage = """
             <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>Comments</title>
               
            </head>

                        <body>
                       <a href="Comments">Comments</a>
                           
                        </div>
                         <center>
                        <div>
                            <form action="/comments" method="POST">
                                <h1>Share your comment with us</h1>
                                    <h2>comment:</h2>
                                    <textarea name="comment" placeholder="Your Comment"  style="height: 200px; width: 500px"></textarea>


                                    <h2 id="passbox">Password:</h2>
                                    <input type="password" placeholder="Password" name="password"><br><br>
                                    <input class="submit" type="submit" value="SEND">
                            </form>
                        </div>
                        <h2>Comments until now</h2>
                            <div >
                                <p class="commentsbox"></p>


                            </div>
                        </center>

                        </body>

            </html>

    """
    return commentspage

def commentedpage(usercoms):
    commentedpage = """
     <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>Comments</title>
                        <body>
                       
                                <li><a href="Comments">Comments</a></li>
                           
                        </div>
                        <center>
                        <div>
                            <form action="/comments" method="POST">
                                <h1>Share your comment with us</h1>
                                    <h2>comment:</h2>
                                    <textarea name="comment" placeholder="Your Comment" style="height: 200px; width: 500px"></textarea>


                                    <h2 id="passbox">Password:</h2>
                                    <input type="password" placeholder="Password" name="password"><br><br>
                                    <input class="submit" type="submit" value="SEND">
                            </form>
                        </div>
                            <div >
                            <h2>Comments until now</h2>
                                <p class="commentsbox">%s</p>


                            </div>
                        </center>

                        </body>

            </html>
           """ % (usercoms)
    return commentedpage
control=0
comlist=[]
def comments():
    confirm_user_pw_hexdigit = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"  
    user_com = request.POST["comment"]
    user_pw = request.POST["password"]
    user_pw_hexdigit = create_hash(user_pw)

    if confirm_user_pw_hexdigit == user_pw_hexdigit:
        comlist.append(user_com)
        commentbox = "<br>"
        for x in comlist:
            commentbox += x+"<br><br><br>"
        return commentedpage(commentbox)

    else:
        return  """ I'm sorry, I can't let you do that!"""




route('/comments', 'POST', comments)
route('/Comments', 'GET', commentspage)



#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()

