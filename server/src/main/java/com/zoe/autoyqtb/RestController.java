package com.zoe.autoyqtb;

import com.zoe.autoyqtb.vo.AddUser;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@org.springframework.web.bind.annotation.RestController
public class RestController {

    @PostMapping("/new")
    Object AddUser( AddUser vo) {
        System.out.println(vo);
        return "ok";
    }

}
