<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=30&pause=1000&color=0E75B6&center=true&vCenter=true&width=900&lines=Hey+%F0%9F%91%8B+I'm+Swapnil+Thakur;Java+Backend+Engineer+%7C+Spring+Boot+%7C+Security;I+build+systems+that+hold+up+under+load." alt="Typing SVG" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/swapnil-thakur-)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=firefox&logoColor=white)](https://swapnil-portfolio-three.vercel.app/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:thakur7swapnil@gmail.com)
[![Resume](https://img.shields.io/badge/Resume-4CAF50?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1zte_k-vEuN_rSRI_Gj3E3oEWtIgBTYr3/view?usp=sharing)
[![Profile Views](https://komarev.com/ghpvc/?username=swapnil1thakur&label=Profile%20Views&color=0e75b6&style=for-the-badge)](https://github.com/Swapnil1Thakur)

</div>

---

## 👨‍💻 About Me

```java
@Component
public class SwapnilThakur implements BackendEngineer {

    private final String role     = "Java Backend Engineer | Spring Boot · Security · REST APIs";
    private final String status   = "Open to SDE Internships & Java Backend Fresher Roles";
    private final String focus    = "Payments · Auth Systems · Distributed Architecture";

    @Override
    public String currentlyBuilding() {
        return "Microservices with Spring Boot + Docker + RabbitMQ";
    }

    @Override
    public String[] whatMakesMeDifferent() {
        return new String[]{
            "Built a UPI-style offline payment backend — idempotency, SHA-256, optimistic locking",
            "OWASP-aligned auth system: HttpOnly cookies, XSS/CSRF mitigated at architecture level",
            "Spring Security + RBAC across 4 privilege levels with 80%+ test coverage",
            "Oracle OCI Certified — Cloud Infrastructure, Gen AI, Cloud Computing"
        };
    }
}
` ` `

---

## 🚀 Featured Projects

<table>
<tr>
<td width="50%" valign="top">

### 💳 [UPI Offline Mesh](https://github.com/Swapnil1Thakur/)
> **Distributed Payment Backend Simulator**

Built for the hard parts of payments — concurrent transactions, partial network failures, and data integrity without a live gateway.

**What's interesting here:**
- 🔒 SHA-256 per-transaction hashing → tamper-proof audit trail
- ⚙️ Optimistic locking → eliminates double-spend under parallel load
- 🔁 Idempotency logic → safe retries on network failure
- 🏗️ Layered Spring Boot architecture (service · repo · controller)

`Java` `Spring Boot` `MySQL` `SHA-256` `Optimistic Locking` `JPA`

</td>
<td width="50%" valign="top">

### 🔐 [AuthBridge](https://github.com/Swapnil1Thakur/auth-app-backend)
> **Full-Stack Authentication System**

Production-ready auth — credential login + OAuth2 SSO (Google & GitHub), built OWASP-first.

**What's interesting here:**
- 🍪 HttpOnly cookie-based refresh token rotation → XSS & CSRF mitigated architecturally
- 🔑 Full JWT lifecycle — silent refresh, token rotation, protected routes
- 🐳 Dockerised full-stack deployment (Spring Boot + React/Vite)
- ✅ OWASP Top 10 guidelines applied at design level

`Spring Boot 3` `Spring Security 6` `OAuth2` `JWT` `Docker` `React` `Vite`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🛒 [ShopNest](https://github.com/Swapnil1Thakur/sb-ecom)
> **E-Commerce Backend Platform**

Full backend — catalog, cart, orders. Focus was on auth integrity and query performance under load.

**What's interesting here:**
- ⚡ 40% faster API response with server-side pagination & filtering
- 🛡️ RBAC across 4 privilege levels via Spring Security + JWT
- ✅ 80%+ JUnit & Mockito test coverage
- 📄 All 15+ endpoints documented via Swagger/OpenAPI

`Java` `Spring Boot` `Spring Security` `JWT` `MySQL` `JUnit` `Mockito` `Swagger`

</td>
<td width="50%" valign="top">

### 📌 What I'm working on next
> **Microservices Migration**

Breaking ShopNest into microservices — separate services for Auth, Catalog, Orders — connected via RabbitMQ with an API Gateway.

**Goal:** demonstrate service isolation, async messaging, and distributed tracing in a real codebase.

`Spring Cloud` `RabbitMQ` `Docker Compose` `API Gateway` `Eureka`

*In progress...*

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

### ⚙️ Core Backend
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)
![Spring Security](https://img.shields.io/badge/Spring_Security-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![Spring Data JPA](https://img.shields.io/badge/Spring_Data_JPA-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![Hibernate](https://img.shields.io/badge/Hibernate-59666C?style=for-the-badge&logo=hibernate&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![OAuth2](https://img.shields.io/badge/OAuth2-EB5424?style=for-the-badge&logo=auth0&logoColor=white)
![REST APIs](https://img.shields.io/badge/REST_APIs-005571?style=for-the-badge&logo=fastapi&logoColor=white)

### 🗄️ Database
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)

### ☁️ DevOps, Messaging & Cloud
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apache-maven&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

### 🧪 Testing & Docs
![JUnit](https://img.shields.io/badge/JUnit5-25A162?style=for-the-badge&logo=junit5&logoColor=white)
![Mockito](https://img.shields.io/badge/Mockito-78A641?style=for-the-badge&logo=java&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)

---

## 🏅 Certifications

| Certification | Issuer | Date |
|---|---|---|
| ☁️ Oracle Cloud Infrastructure 2024 Foundations Associate | Oracle | Oct 2025 |
| 🤖 Generative AI Professional | Oracle | Sept 2025 |
| 🌐 Cloud Computing | NPTEL | July 2025 |

---

## 📊 GitHub Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=swapnil1thakur&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" height="165" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=swapnil1thakur&layout=compact&theme=tokyonight&hide_border=true&langs_count=6" height="165" />

</div>

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=swapnil1thakur&theme=tokyonight&hide_border=true" />

</div>

---

## 🏆 By the Numbers

<div align="center">

| 💳 Payment Systems | 🔐 Auth & Security | ⚡ Performance | 🧪 Test Coverage | 🧩 DSA Problems |
|:---:|:---:|:---:|:---:|:---:|
| 1 production-grade offline UPI simulator | OWASP-aligned, HttpOnly cookies, XSS/CSRF mitigated | 40% API response improvement | 80%+ JUnit & Mockito | 300+ (LeetCode + GFG) |

</div>

---

## 💼 What I'm Looking For

I'm actively seeking **SDE Internships** and **Java Backend Fresher roles** where I can contribute to backend systems — APIs, auth, payments, or distributed architecture.

If your team works with **Java / Spring Boot** and cares about building things right — I'd love to connect.

📬 **thakur7swapnil@gmail.com** · [LinkedIn](https://linkedin.com/in/swapnil-thakur-) · [Portfolio](https://swapnil-portfolio-three.vercel.app/)

---

<div align="center">

*"Build systems that are secure by design, not by accident."*

</div>
```

**Note:** About Me section ke andar jo java code block hai, usme backticks ` ` ` (space ke saath) likhe hain — paste karne ke baad unhe ` ``` ` (bina space) kar dena. Nested code block GitHub markdown ki limitation hai.
