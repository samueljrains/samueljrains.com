#! /usr/bin/python
# -*- coding: utf-8 -*-


import sys
import random

sys.dont_write_bytecode = True

# import connection string 'con' with stored credentials
from connect import con  
print """
<!DOCTYPE html>
<!--
 * Copyright 2014 
 * Licensed under the Apache License v2.0
 * Redesigned, Developed, and Maintained by: Samuel Jackson Rains
 * Original design by Carlos Alvarezand http://www.basicoh.com.
--> 
<html lang="en">
    <head>
        <title>Samuel J. Rains</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="keywords" content="software portfolio, portfolio, jack rains, web development, web design, php, objective-c, app, samuel rains, atlanta, georgia" />
        <meta name="description" content="Samuel J. Rains is a software developer from Atlanta, Georgia.   The site contains information regarding various software projects and bodies of work." />
        <meta name="author" content="Samuel J. Rains">

        <!-- CSS files-->
        <link href="css/bootstrap.css" rel="stylesheet">
        <link href="css/component.css" rel="stylesheet">
        <link href="css/bootstrap-responsive.css" rel="stylesheet">
        <link href="css/alertify.core.css" rel="stylesheet">
        <link href="css/prism.css" rel="stylesheet" />        
        <script type="text/javascript" src="js/modernizr.custom.js"></script>

        <!--[if IE 9]>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        
        <!-- favicon and touch icons -->
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="images/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="images/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="images/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="images/apple-touch-icon-57-precomposed.png">
        <link rel="icon" href="images/favicon.png">         
        <script type="text/javascript" >
            (function(i,s,o,g,r,a,m)
                {i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                })
                (window,document,'script','//www.google-analytics.com/analytics.js','ga');
                ga('create', 'UA-47836191-1', 'samueljrains.com');
                ga('send', 'pageview');
        </script>
    </head>
    <body>
        <div class="container">
            <div id="bl-main" class="bl-main">
            <!--=========== ABOUT SECTION ===========-->
                <section>
                    <div class="bl-box">
                        <h2 >About</h2> <!-- class="bl-icon bl-icon-about" -->
                    </div><!-- /bl-box -->
                    <div class="bl-content">
                        <div class="row-fluid">
                            <div class="span12">
                                <h2>Hi there!</h2>
                                <p>
                                <!--<img src="images/me.png" style="display: inline; float: left;"/>-->
                                I'm Jack Rains and I'm a developer out of Atlanta, Georgia.  I've been working in the field full-time since 2008 and part-time since 2006.  I mainly use open-source technologies but have worked in proprietary stacks as well.  Hope you enjoy my site.</p>
                                <div class="row-fluid">
                                    <div class="span8">
                                        <h2>My Skills</h2>
                                        <!-- Progress Bar --> 
                                        <div class="progress">
                                        <div class="bar" style="width: 75%;">PHP 75%</div>
                                        </div>
                                        <div class="progress">										
                                        <div class="bar" style="width: 80%;">HTML/CSS 80%</div>								
                                        </div>  
                                        <div class="progress">										
                                        <div class="bar" style="width: 65%;">MySQL 65%</div>		                                        
                                        </div>
                                        <div class="progress">
                                        <div class="bar" style="width: 50%;">Python 50%</div>
                                        </div>                                                                                 
                                        <div class="progress">										
                                        <div class="bar" style="width: 85%;">Web Accessibility 85%</div>
                                        </div>  										
                                        <div class="progress">
                                        <div class="bar" style="width: 50%;">Git 50%</div>
                                        </div>                                         
                                        <!-- Progress Bar End --> 
                                    </div><!-- /span6 -->
                                    <div class="span4"></div>
                                    <div class="span12">
                                        <br>
                                        <br>
                                    </div>
                                    <div class="span12">
                                        <div class="row about-us">
                                                <div class="span3">
                                                <h3><i class="icon-user icon-white"></i> More About Me</h3>
                                                Based out of Atlanta and a product of the University of Alabama, I'm an avid disc (and ball) golf player.  I also enjoy bicycling, technology, surf music, and attempting to stay in shape...the latter being easier said than done.  I've also been known to enjoy a craft beer or coffee around town.
                                                </div>
                                                <div class="span3">
                                                <h3><i class="icon-heart icon-white"></i> What I Love</h3>
                                                Collaborating with like-minded individuals to create the best possible solutions to any given issue is what drives me.  I love creating software and approaching tasks with an open and positive mind. Accessibility and equal access for all are passions of mine.
                                                </div>
                                                <div class="span3">
                                                <h3><i class="icon-wrench icon-white"></i> Work</h3>
                                                I'm working with the Georgia Institute of Technology to help bring accessible SaaS to individuals across the U.S.  In addition, I building my online presence and portfolio through various independent and collaborative projects.  I'm wanting to expand my front-end knowledge as well.
                                                </div>   
                                                <div class="span3">
                                                <h3><i class="icon-bullhorn icon-white"></i> Get In Touch</h3>
                                                Feel free to drop me a line at jack@samueljrains.com.  I'm always up for exchanging ideas or possible collaborations.  I don't bite!
                                                </div>    
                                        </div><!-- /row-about-us -->  
                                    </div><!-- /span12 -->
                                </div><!-- /row -->
                            </div><!-- /span12 -->
                        </div><!-- /row-fluid -->
                    </div><!-- /bl-content --> 
                    <span class="bl-icon bl-icon-close"></span>
                </section>

                <!--=========== PORTFOLIO SECTION ===========-->
                <section id="bl-work-section">
                    <div class="bl-box">
                            <h2>Projects</h2> <!-- class="bl-icon bl-icon-works"-->
                    </div>
                    <div class="bl-content" >
                        <h2>Recent Projects</h2>
                        <p>Here are some of the recent projects I have been working on full-time.  They encompass my abilities, not only in web development and software, but design as well.  These web based applications are cross-compatible.  "Speaking to" each other despite different database architecture and languages.</p>
                        <p>I've taken an interest in PostgreSQL and Python development of late.  iOS and Android (Java!) development are also on the horizon...within the year, I'm aiming to add to my portfolio with mobile apps.  In the meantime, here are some examples of my body of work.</p>
                        <div class="row-fluid">
                            <div class="span4">
                                <ul id="bl-work-items" style="list-style: none;">
                                    <li data-panel="panel-1"><a href="#"><img src="images/projects/atn.png" alt="access text dashboard" /></a></li>
                                </ul>
                                <p>AccessText Network</p>							
                            </div><!-- /span4 -->
                            <div class="span4">
                                <ul id="bl-work-items">
                                    <li data-panel="panel-2"><a href="#"><img src="images/projects/amac.png" alt="amac homepage" /></a></li>
                                </ul>
                                <p>Alternative Media Access Center</p>							
                            </div><!-- /span4 -->
                            <div class="span4">
                                <ul id="bl-work-items">
                                    <li data-panel="panel-3"><a href="#"><img src="images/projects/student_center.png" alt="student download center portal page"/></a></li>
                                </ul>
                                <p>Student Download & Resource Center</p>							
                            </div><!-- /span4 -->                            
                        </div><!-- /row-fluid -->
<!--AccessGA, App(s), Invertr stuff when completed.   Hurry it up will ya'?!                        
								<div class="row-fluid">
                            <div class="span4">
                                <ul id="bl-work-items" style="list-style: none;">
                                    <li data-panel="panel-1"><a href="#"><img src="images/projects/atn.png" alt="accessga homepage" /></a></li>
                                </ul>
                                <p>AccessGA</p>							
                            </div> 
                            <div class="span4">
                                <ul id="bl-work-items" style="list-style: none;">
                                    <li data-panel="panel-1"><a href="#"><img src="images/projects/atn.png" alt="accessga homepage" /></a></li>
                                </ul>
                                <p>AccessGA</p>							
                            </div>   
                            <div class="span4">
                                <ul id="bl-work-items" style="list-style: none;">
                                    <li data-panel="panel-1"><a href="#"><img src="images/projects/atn.png" alt="accessga homepage" /></a></li>
                                </ul>
                                <p>AccessGA</p>							
                            </div>                                                                              
                     	</div>
-->
                    </div><!-- /bl-content -->
                    <span class="bl-icon bl-icon-close"></span>
                </section>

                    <!--=========== BLOG SECTION ===========-->
                <section>
                    <div class="bl-box">
                        <h2>Articles</h2>
                    </div>
                    <div class="bl-content">
                        <div class="row-fluid">
                            <div class="span12">
                                <h2>Stuff</h2>
                                    <img src="images/water-pic2.jpg" style="width: 100%;" alt="blue waterfront with dock">                                
                                <article>
"""
#uses 'connect' script and creates a cursor to pull latest article from 'articles' DB table.  outputs previous ones below it as well.
with con:
    cur = con.cursor()
    cur.execute("SELECT id, title, article, date FROM articles ORDER BY id DESC LIMIT 1")
    for i in range(cur.rowcount):
        row = cur.fetchone()
        print "<h3>%s</h3>" % (row[1])
        print "<p>%s</p>" % (row[3].strftime("%m.%d.%y"))
        print row[2]
        cur.close()                                   
print """        
                                </article>
                                <hr>
                                <h2>Other Entries</h2>
<div class='panel-group' id='accordion'>                               

"""
with con:
    old_articles = con.cursor()
    old_articles.execute("SELECT id, title, article, date FROM articles ORDER BY date DESC LIMIT 10 OFFSET 1")
for item in old_articles:
		print "<article><div class='panel panel-default'><div class='panel-heading'><h3 class='panel-title'><a style='color: white;' data-toggle='collapse' data-parent='#accordion' href='#collapse%s'>%s %s</a></h3></div><div id='collapse%s' class='panel-collapse collapse'><div class='panel-body'>%s<hr></div></div></div></article>" % (item[0], item[1] , item[3].strftime("%m.%d.%y"), item[0], item[2])
#		print "<article><div class='panel panel-default'><div class='panel-heading'><h3 class='panel-title'><a style='color: white;' data-toggle='collapse' data-parent='#accordion' href='#collapse%s'>%s</a></h3></div><div id='collapse%s' class='panel-collapse collapse'><div class='panel-body'>%s<br />%s<hr></div></div></div></article>" % (item[0], item[1] , item[0], item[3].strftime("%m.%d.%y"), item[2])		
old_articles.close()
con.close()		
print """        
</div>                                                                   
                            </div><!-- /span12 -->
                            
                        </div><!-- /row-fluid -->
                    </div><!-- /bl-content -->
                    <span class="bl-icon bl-icon-close"></span>
                </section>
                <!--=========== CONTACT SECTION ===========-->
                <section>
                    <div class="bl-box">
                        <h2 >Contact</h2>
                    </div>
                    <div class="bl-content">
                        <div class="row-fluid">
                            <div class="span12">
                                <h2>Get in touch</h2>
                                <img src="images/atl.jpg" style="width: 100%;" alt="atlanta skyline" />		                                
                                <br>
                                """
#used for generating two random numbers (1-10) and ask user to add together to try and trick any spam bots
number1 = random.randrange(1,10+1)
number2 = random.randrange(1,10+1)
answer_value = number1 + number2
print """                                
                                <script type="text/javascript">
                                var number1 = Math.floor((Math.random() * 10) +1);
                                var number2 = Math.floor((Math.random() * 10) + 1);
                                var answer = number1 + number2;
                                </script>
                                <p>Fill out the form below, or you could drop me an email as well.</p>								
                                <form id="myForm" method="post" title="Contact Info Request Form"  action="action.cgi">
                                		<fieldset>
                                		<legend></legend>
                                    <input type="text"  title="field for entering your name" name="name" id="name" maxlength="50" placeholder="Name" />
                                    <br />
                                    <input type="email" title="field for entering your email address" name="email" id="email" maxlength="50" placeholder="Email" />
                                    <br />
                                    <textarea title="field for entering your message" name="message" id="message" rows="5" cols="4" maxlength="1000"placeholder="Message"></textarea>
                                    <br />
                                    """
print "What is %d + %d?" % (number1, number2)
print """
												<br />
                                    <input style="width: 70px;" type="text" title="field for entering the anti spam answer" placeholder="Answer" size="4" maxlength="2" id="answer_input" name="answer_input" />						                                    
"""
print "<input type='hidden' name='answer_value' id='answer_value' value='%d'/>" % (answer_value)
print """
                                    <br />
                                    <br />
                                    <input type="submit" class="submit" name="submit" value="send message" />
                                    </fieldset>
                                </form>				
<!--FINISH THIS!!!  FORM WITH TABLE AND LABELS 
                                <form id="myForm" method="post" title="Contact Info Request Form"  action="action.cgi">
                                <table summary="Contact Infomration">							
                                		<fieldset>
                                		<legend></legend>
                                		<tr><td colspan="2">
                                    <label for="name">Name</label></td>
                                    <td><input type="text"  title="field for entering your name" name="name" id="name" maxlength="50" />
                                    </td></tr>
                                    <tr><td colspan="2">
                                    <label for="email">Email</label></td><td><input type="email" title="field for entering your email address" name="email" id="email" maxlength="50" placeholder="Email" />
                                    </td></tr>
                                		<tr><td colspan="2">
                                    <label for="message">Message</label></td><td><textarea title="field for entering your message" name="message" id="message" rows="5" cols="4" maxlength="1000"placeholder="Message"></textarea>
                                    </td><t/r>
                                		<tr><td>                                    
                                    """
print "What is %d + %d?</td></tr>" % (number1, number2)
print """
                                		<tr><td colspan="2">
                                    <label for="answer_input">Answer</label></td><td><input style="width: 70px;" type="text" title="field for entering the anti spam answer" placeholder="Answer" size="4" maxlength="2" id="answer_input" name="answer_input" />						                                    
"""
print "<input type='hidden' name='answer_value' id='answer_value' value='%d'/>" % (answer_value)
print """
                                		<tr><td>
                                    <input type="submit" class="submit" name="submit" value="send message" />
                                    </td></tr>
                                    </fieldset>
                                    </table>
                                </form>	
-->                                                                			
                                <p>jack@samueljrains.com | Atlanta, Georgia 30307</p>
                                <p>
                                    <a href="http://www.github.com/samueljrains" class="social-network github" target="_blank" ><span>github</span></a>
                                    <a href="http://www.reddit.com/user/alasjr" class="social-network reddit" target="_blank" ><span>reddit</span></a>
                                    <a href="http://www.twitter.com/jack__rains" class="social-network twitter" target="_blank" ><span>twitter</span></a>                                    
                                    <a href="https://stackexchange.com/users/3475503/jack?tab=accounts" class="social-network openid" target="_blank"><span>stack exchange</span></a>								
                                </p>
                            </div>
                        </div>
                    </div>
                    <span class="bl-icon bl-icon-close"></span>
                </section>                 
                    <!--=========== PROJECTS DESCRIPTIONS SECTION ===========--> 
                <div class="bl-panel-items" id="bl-panel-work-items">
                    <div data-panel="panel-1">
                        <div class="row-fluid">
                            <div class="span8 offset2 tweak">
                                <img src="images/projects/atn.png" alt="accesstext dashboard" />
                                <br>
                                <br>
                                <h3>The AccessText Network</h3>
                                <p>AccessText is a conduit between the publishing world and colleges and universities across the country, with a shared mission to ensure students with disabilities have equal access to their textbooks in an accessible format and in a timely manner.</p>
                                <h4>Project Details</h4>                                
                                <p>Accommodating several textbook publisher's APIs, I developed a tracking and real-time delivery system with extensive user management to provide accessible textbooks and requests to end users.  This includes, download restrictions (14 days only), request data, geographical/IP information, etc. </p>
                                <p>Using the CakePHP framework, I migrated off the existing (and outsourced) architecture of the network and developed an extensive backend for user management, file delivery, and asset tracking.  I also assisted in the front-end design and implementation of the forward facing website.</p>
                                <p><a href="http://accesstext.org" title="accesstext homepage" target="_blank" >AccessText Website</a></p>
                            </div><!-- /span8 -->
                        </div><!-- /row-fluid -->	
                    </div><!-- /panel1 -->
                    <div data-panel="panel-2">
                        <div class="row-fluid">
                            <div class="span8 offset2 tweak">
                                <img src="images/projects/amac.png" alt="professional work screenshot"/>
                                <br>
                                <br>
                                <h3>Alternative Media Access Center</h3>
                                <p>The Alternative Media Access Center is an organization based on removing the barriers in education for indivduials with disabilities.</p>
                                <h4>Project Details</h4>
                                <p>As one of only three developers, I have rewritten the realtime delivery of accessible media and facilitated the storage and access of over 15,000 accessible media files and hundres of thousands of mission critical data files.  Primarily with the use of a LAMP stack (with Ruby scripts for backup) and agile development practices, I have helped create a single system for internal assets, employee information, sensitive student data, ticketing and support logging, in addition to accessible textbooks and media.  The AMAC project encompasses hundreds of membership organizations across the United States and is growing rapidly.  With the growth, scalability of the database architecture and systems has become paramount to my position and continues to do so everyday.</p>
                                <p>The unit was recently awarded the 2014 Campus Technology Innovator Award Winner in the Student Systems & Services category for the efficiency and ease-of-use by the products and services I have developed and maintained for several years. Also, the award was given due to the excellent analytics software reporting and quickness in response time.  More information can be found here.  <a href="http://us5.campaign-archive1.com/?u=c8be6d0b95d2e799aabd3f20f&id=44e07f76e8" title="link to annoucment for award" target="_blank">Award Announcement</a></p>
                                <p><a href="http://www.amacusg.gatech.edu" target="_blank" >AMAC Website</a></p>
                            </div><!-- /span8 -->
                        </div><!-- /row-fluid -->	
                    </div><!-- /panel2 -->           
                    <div data-panel="panel-3">
                        <div class="row-fluid">
                            <div class="span8 offset2 tweak">
                                <img src="images/projects/student_center.png" alt="screenshot of student center dashboard">
                                <br>
                                <br>
                                <h3>Student Download & Resource Center</h3>
                                <p>The Student Download & Resource Center is a web application that was designed and developed to integrate the existing ordering systems directly with students.  The process streamlines ordering and conveniently places all information directly in the hands of the students.  Also, the portal allows students to request orders, software, as well as download their media.</p>
                                <h4>Project Details</h4>
                                <p>The Student Download & Resource Center is a "ground up" PHP project using MySQL as the database.  The front end uses jQuery and JavaScript functions to create a seamless product that is both easy-to-use and highly functional as well.</p>
                                <p><a href="http://www.amacusg.gatech.edu" target="_blank" >AMAC Website</a></p>                                                           
                            </div><!-- /span8 -->
                        </div><!-- /row-fluid -->	
                    </div><!-- /panel3 -->                                           
                    <nav>
                        <span class="bl-next-work">Next Project</span>
                        <span class="bl-icon bl-icon-close"></span>
                    </nav>
                </div><!-- /panel-items -->
            </div><!-- /bl-main -->
        </div> <!-- /container -->

        <!-- javascript files-->
        <script type="text/javascript" src="js/jquery-1.8.2.min.js"></script>
        <script type="text/javascript" src="js/bootstrap.min.js"></script>
        <script type="text/javascript" src="js/boxlayout.js"></script>
        <!--JS files for contact form -->
        <script type="text/javascript" src="js/contact.js"></script>   
        <script type="text/javascript" src="js/jquery.form.js"></script> 
        <script type="text/javascript" src="js/alertify.min.js"></script>
        <script>
        $(function() {
            Boxlayout.init();
        });
        </script>
		 <script src="js/prism.js"></script>        
    </body>
</html>
"""


