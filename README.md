# Backend-Developer-Intern---Assignment---VRV-Security
This assignment is based on the concept of RBAC (Role Bases Access Control) for VRV Security's Backend Developer Role. It is developed on Django (a python's framework) and modified the admin portal according to the requirement. 

The default setup is as follows -
## _Role Details_
| Role | Permissions |
| ---- | ---- |
| Admin | Can Add/View/Change Group, Add/View/Change/Delete Users |
| Moderator | Can View Group, Add/View/Change Users |
| User | Can Vew Group, View User |

## _User Details_
| Email | Password | Role | Comment |
| ----- | ----- | ----- | ---- |
| user@test.com | User@12345 | User |
| moderator@test.com | Mode@12345 | Moderator | 
| admin@test.com | Admin@12345 | Admin | 
| avshankar9151@gmail.com | | | This account is superuser and can't be modified/deleted by anyother above users. Only Superuser can modify/delete another superuser's account. |

Project Demo Link - https://rbac-vrv.htpsystem.com/

> Note: In case if above setup for user/gruops are not working, due to any chagne done in testing, please reach out to me to reset this to default setup on my email avshankar9151@gmail.com
