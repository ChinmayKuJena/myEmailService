package com.emailSender.emailSender.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;
import java.util.*;

@Service
public class EmailService {

    @Autowired
    private JavaMailSender emailSender;

    public void sendSimpleEmail(String to, String subject, String text) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(to);
        message.setSubject(subject);
        message.setText(text);
        emailSender.send(message);
    }

    // Method to send a simple email with CC support
    public void sendEmailToMultiple(String to, List<String> cc, String subject, String text) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(to); // Primary recipient
        message.setSubject(subject);
        message.setText(text);
        // Add CC if provided
        if (cc != null && !cc.isEmpty()) {
            String[] ccArray = cc.toArray(new String[0]);
            message.setCc(ccArray);
        }
        emailSender.send(message);
    }
}
