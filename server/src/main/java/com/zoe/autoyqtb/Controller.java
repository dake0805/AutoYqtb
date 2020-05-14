package com.zoe.autoyqtb;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@org.springframework.stereotype.Controller
public class Controller {

    @Autowired
    Repo repo;

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @PostMapping("/")
    public String index(@RequestParam("account") String account,
                        @RequestParam("password") String password,
                        @RequestParam("location") String location) {


        User user = new User(account, password, location);
        repo.save(user);
        return "finish";
    }
}
