package com.zoe.autoyqtb;

import com.zoe.autoyqtb.vo.AddUser;
import com.zoe.autoyqtb.vo.UserLogin;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;

@org.springframework.web.bind.annotation.RestController
public class RestController {

    @Autowired
    Repo repo;

    @PostMapping("/new")
    Object AddUser(AddUser vo) {
        String account = vo.getAccount();
        User old = repo.findByAccount(account).orElse(null);
        if (old != null) {
            return "user already exist.";
        }

        User user = new User(account, vo.getPassword(), vo.getLocationName(), vo.getLocationCode());
        if (vo.isInSchool()) {
            user.isInSchool();
        } else {
            user.notInSchool();
        }
        repo.saveAndFlush(user);
        return "finish";
    }

    @PostMapping("/login")
    Object login(UserLogin login) {
        User u = repo.findByAccount(login.getAccount()).orElse(null);
        if (u != null && u.getPassword().equals(login.getPassword()))
            return u;
        return null;
    }

}
