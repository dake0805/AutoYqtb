package com.zoe.autoyqtb;

import com.zoe.autoyqtb.vo.AddUser;
import com.zoe.autoyqtb.vo.EditUser;
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

    @PostMapping("/edit")
    Object edit(EditUser edit) {
        if (edit.getAccount() == null || edit.getOldPassword() == null) {
            return "wrong params.";
        }
        User u = repo.findByAccount(edit.getAccount()).orElse(null);
        if (u == null || edit.getOldPassword() == null) {
            return "wrong params.";
        }
        if (u.getPassword().equals(edit.getOldPassword())) {
            if (edit.isWantStop()) {
                repo.delete(u);
                return "deleted.";
            }
            u.setLocation(edit.getLocationName());
            u.setZip(edit.getLocationCode());
            u.setPassword(edit.getNewPassword());
            u.setInschool(edit.isInSchool() ? 1 : 0);
            return repo.saveAndFlush(u).toString();
        } else {
            return "Wrong password. Don't do that.";
        }
    }

}
