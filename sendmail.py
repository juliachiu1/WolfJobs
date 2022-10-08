import smtplib
from email.message import EmailMessage


class Sendemail:
    def __init__(self):
        self.gmail_address = 'csc510demo841231@gmail.com'
        self.gmail_password = 'pfkcqvblqqvqtvig'
        self.sent_name = 'WolfJobs'

    def send_mail_regis(self, regis_mail, name):
        msg = EmailMessage()
        msg['Subject'] = 'WolfJobs Registration Confirmation Letter'
        msg['From'] = self.gmail_address
        msg['To'] = regis_mail
        msg_content = '''
               <!DOCTYPE html>
               <html>
                   <body>
                       <div style="padding:20px 0px">
                           <div style="height: 500px;width:800px">
                               <div style="text-align:left;">
                                   <p>Dear {}, <br><br> We are glad you signed up for WolfJobs. 
                                   To start exploring the power of WolfJobs, you can click the following link:
                                   <br>
                                   <a href="http://127.0.0.1:5000/login" target="_blank">View WolfJobs Website</a>
                                   <br><br>
                                   Welcome to WolfJobs
                                   <br><br>
                                   The WolfJobs Team
                                   </p>                          
                               </div>
                           </div>
                       </div>
                   </body>
               </html>
               '''.format(name)
        msg.set_content(msg_content, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.gmail_address, self.gmail_password)
            smtp.send_message(msg)

    def send_mail_apply(self, apply_mail, apply_name, apply_job):
        msg = EmailMessage()
        msg['Subject'] = 'Job Applied Confirmation Letter'
        msg['From'] = self.gmail_address
        msg['To'] = apply_mail
        msg_content = '''
                       <!DOCTYPE html>
                       <html>
                           <body>
                               <div style="padding:20px 0px">
                                   <div style="height: 500px;width:800px">
                                       <div style="text-align:left;">
                                           <p>Dear {}, <br><br> Thanks for your interest in the {} position! 
                                           <br><br>
                                           A quick note about what happens next: 
                                           <br><br>
                                           We carefully review every application - including yours. We're fortunate 
                                           to have many outstanding people apply to each of our positions, 
                                           and we're sure that you're no exception. While we appreciate 
                                           every application that comes our way, due to the high volume 
                                           we receive we're not able to follow up with everyone individually. 
                                           If a strong match is found between your qualifications and the needs 
                                           of the role, we'll contact you. 
                                           <br><br>
                                           If you are not offered an opportunity at this time, we may keep 
                                           your information on file to evaluate you for other positions.
                                           <br>
                                           Thanks again for your interest in using WolfJobs to apply jobs, and we 
                                           wish you success in your job search!
                                           <br><br>
                                           Sincerely,
                                           <br><br>
                                           The WolfJobs Team
                                           </p>                          
                                       </div>
                                   </div>
                               </div>
                           </body>
                       </html>
                       '''.format(apply_name, apply_job)
        msg.set_content(msg_content, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.gmail_address, self.gmail_password)
            smtp.send_message(msg)

    def send_mail_interview(self, interview_mail, interview_job, interview_name):
        msg = EmailMessage()
        msg['Subject'] = 'Job Interview Confirmation Letter'
        msg['From'] = self.gmail_address
        msg['To'] = interview_mail

        msg_content = '''
                       <!DOCTYPE html>
                       <html>
                           <body>
                               <div style="padding:20px 0px">
                                   <div style="height: 500px;width:800px">
                                       <div style="text-align:left;">
                                           <p>Dear {}, 
                                           <br><br> Thank you for your application for the {} position 
                                           at AA Company. 
                                           <br>
                                           We are impressed by your background and think that your qualifications 
                                           make you an excellent candidate for this role. We would like to invite 
                                           you to interview at our office.
                                           <br><br>
                                           During the interview, you will have the opportunity to learn more about the 
                                           role at hand and our company. We, of course, will have the pleasure of 
                                           getting to know more about you and your background and whether this position 
                                           aligns with your professional goals.
                                           <br><br>
                                           If you have any questions before the interview, please do not hesitate to 
                                           contact me. I look forward to meeting you.
                                           <br><br>
                                           Sincerely,
                                           <br><br>
                                           The WolfJobs Team
                                           </p>                          
                                       </div>
                                   </div>
                               </div>
                           </body>
                       </html>
                       '''.format(interview_name, interview_job)
        msg.set_content(msg_content, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.gmail_address, self.gmail_password)
            smtp.send_message(msg)

    def send_mail_reject(self, reject_mail, reject_name):
        msg = EmailMessage()
        msg['Subject'] = 'Job Rejection Letter'
        msg['From'] = self.gmail_address
        msg['To'] = reject_mail

        msg_content = '''
                       <!DOCTYPE html>
                       <html>
                           <body>
                               <div style="padding:20px 0px">
                                   <div style="height: 500px;width:800px">
                                       <div style="text-align:left;">
                                           <p>Dear {}, 
                                           <br><br> We appreciate the time and effort you dedicated to the application 
                                           process with WolfJobs! We know there are a lot of companies out there 
                                           and we are happy that you chose us. 
                                           <br><br>
                                           Unfortunately, we will not be proceeding with your application at this time. 
                                           The decision to pass on your candidacy was not an easy one.
                                           <br><br>
                                           If you would like to be considered for this role in the future, please apply 
                                           with an updated resume after 6 months.
                                           <br><br>
                                           You can check back for opportunities on our Careers page.
                                           <br><br>
                                           We look forward to staying in touch!
                                           <br><br>
                                           Sincerely,
                                           <br><br>
                                           The WolfJobs Team
                                           </p>                          
                                       </div>
                                   </div>
                               </div>
                           </body>
                       </html>
                       '''.format(reject_name)
        msg.set_content(msg_content, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.gmail_address, self.gmail_password)
            smtp.send_message(msg)

    def send_mail_forget_password(self, forget_mail):
        msg = EmailMessage()
        msg['Subject'] = 'WolfJobs - Reset Password Request'
        msg['From'] = self.gmail_address
        msg['To'] = forget_mail

        msg_content = '''
                       <!DOCTYPE html>
                       <html>
                           <body>
                               <div style="padding:20px 0px">
                                   <div style="height: 500px;width:800px">
                                       <div style="text-align:left;">
                                           <p>Dear WolfDogs Users, 
                                           <br><br>
                                           We got a request to reset your WolfJobs password.
                                           Please use the following link to reset your password:
                                           <br>
                                           <a href="http://127.0.0.1:5000/resetpassword" target="_blank">Reset your 
                                           password</a>
                                           <br><br>
                                           If you ignore this message, your password won't be changed.
                                           <br><br>
                                           If you didn't request a password reset, let us know.
                                           <br><br>
                                           Sincerely,
                                           <br><br>
                                           The WolfJobs Team
                                           </p>                          
                                       </div>
                                   </div>
                               </div>
                           </body>
                       </html>
                       '''
        msg.set_content(msg_content, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.gmail_address, self.gmail_password)
            smtp.send_message(msg)







