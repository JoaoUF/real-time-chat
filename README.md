## TODO

- [ ] add chatroom route
- [ ] change url destination from core to msauthentication

## USER REQUIREMENT

These are some of the user requirements I have in mind, probably I will add more or forget to do it:
| **Module** | **Requirement ID** | **Requirement Description** | **Done** |
|-----------------------------|--------------------|--------------------------------------------------------------------------------------------------------------|----------|
| **1. Authentication Module** | 1.01 | Users must authenticate using OAuth2. | [ ] |
| | 1.02 | Verification emails are sent to users to confirm their identity. | [ ] |
| **2. Room Management Module**| 2.01 | Users start in a default AI room upon login. | [ ] |
| | 2.02 | Users can create a new room with one or multiple contacts. | [ ] |
| | 2.03 | Users can name and configure room settings. | [ ] |
| **3. Contact Management Module** | 3.01 | Users can search for contacts through Gmail integration. | [ ] |
| | 3.02 | Existing contacts from the user’s account are available for selection. | [ ] |
| | 3.03 | Users can send contact requests to found contacts. | [ ] |
| **4. Chat Functionality Module** | 4.01 | Users can send and receive text messages in chat rooms. | [ ] |
| | 4.02 | Users can upload images, text files, and emojis in chat rooms. | [ ] |
| | 4.03 | The system should indicate if a message has been sent and read. | [ ] |
| | 4.04 | Messages display the hour they were sent. | [ ] |
| | 4.05 | Chat rooms display the date of the last message. | [ ] |
| **5. User Interface Module** | 5.01 | The interface should display the list of rooms and active chat windows clearly. | [ ] |
| | 5.02 | Users should receive notifications for new messages and contact requests. | [ ] |
| | 5.03 | Users can search for messages and contacts within the system. | [ ] |
| **6. Integration Module** | 6.01 | Seamless integration with Gmail for contact search and management. | [ ] |
| | 6.02 | Integration with AI services for the default room. | [ ] |
| **7. Security and Privacy Module** | 7.01 | Messages and user data must be encrypted during transmission and storage. | [ ] |
| | 7.02 | Implement privacy measures to protect user data and comply with regulations (e.g., GDPR). | [ ] |
| **8. Performance and Usability Module** | 8.01 | The system should handle multiple users and high volumes of messages efficiently. | [ ] |
| | 8.02 | The interface should be intuitive and easy to navigate. | [ ] |
| **9. Administrative Module** | 9.01 | Admins should have the ability to manage users, including activating, deactivating, and viewing user activity. | [ ] |
| | 9.02 | The system should provide usage analytics and reports to administrators. | [ ] |

## References

1. Libraries documentation:
   1. [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/installation.html)
   2. [django-allauth](https://docs.allauth.org/en/latest/socialaccount/providers/google.html)
   3. [simple-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
