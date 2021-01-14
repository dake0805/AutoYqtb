package com.zoe.autoyqtb;

import org.springframework.web.bind.annotation.GetMapping;

@org.springframework.stereotype.Controller
public class Controller {

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @GetMapping("/login")
    public String login() {
        return "login";
    }

//    @PostMapping("/")
//    public String index(@RequestParam("account") String account,
//                        @RequestParam("password") String password,
//                        @RequestParam("province") String province,
//                        @RequestParam("city") String city,
//                        @RequestParam(value = "district", required = false) String district,
//                        @RequestParam(value = "inschool", required = false) String inSchool) {
//
//        User old = repo.findByAccount(account).orElse(null);
//        if (old != null) {
//            return "userExist";
//        }
//
//        User user = new User(account, password, province, city, district);
//        if ("on".equals(inSchool)) {
//            user.isInSchool();
//        } else {
//            user.notInSchool();
//        }
//        repo.saveAndFlush(user);
//        return "finish";
//    }
}
