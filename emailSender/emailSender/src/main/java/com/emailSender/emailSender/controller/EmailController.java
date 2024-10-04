package com.emailSender.emailSender.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.emailSender.emailSender.dto.EmailRequest;
import com.emailSender.emailSender.dto.EmailRequestCC;
import com.emailSender.emailSender.service.EmailService;
import java.util.*;

@RestController
@RequestMapping("/email")
public class EmailController {

    @Autowired
    private EmailService emailService;

    @PostMapping("/send")
    public ResponseEntity<String> sendEmail(@RequestBody EmailRequest emailRequest) {
        try {
            emailService.sendSimpleEmail(emailRequest.getRecipientEmail(), emailRequest.getSubject(),
                    emailRequest.getMessage());
            return ResponseEntity.ok("Email sent successfully!");
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Failed to send email: " + e.getMessage());
        }
    }

    @PostMapping("/send-cc")
    public ResponseEntity<String> sendEmailCC(@RequestBody EmailRequestCC emailRequest) {
        String to = emailRequest.getTo();
        List<String> cc = emailRequest.getCc();
        String subject = emailRequest.getSubject();
        String message = emailRequest.getMessage();

        try {
            emailService.sendEmailToMultiple(to, cc, subject, message);
            return ResponseEntity.ok("Email sent successfully!");
        } catch (Exception e) {
            return ResponseEntity.status(500).body("Failed to send email: " + e.getMessage());
        }
    }
}