package com.zoe.autoyqtb;

import org.springframework.lang.Nullable;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Objects;

@Entity
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;

    private String account;

    private String password;

    private String location;

    private int inschool;

//    private String province;
//    private String city;
//    private String district;

    private String zip;


    public User() {
    }

    public User(String account, String password, String location, String zip) {
        this.account = account;
        this.password = password;
        this.location = location;
        this.zip = zip;
    }


    public void isInSchool() {
        this.inschool = 1;
    }

    public void notInSchool() {
        this.inschool = 0;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return Objects.equals(account, user.account);
    }

    @Override
    public int hashCode() {
        return Objects.hash(account);
    }


    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getAccount() {
        return account;
    }

    public void setAccount(String account) {
        this.account = account;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public int getInschool() {
        return inschool;
    }

    public void setInschool(int inschool) {
        this.inschool = inschool;
    }


    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
    }

    @Override
    public String toString() {
        return "User{" +
                "account='" + account + '\'' +
                ", password='" + password + '\'' +
                ", location='" + location + '\'' +
                ", inschool=" + inschool +
                ", zip='" + zip + '\'' +
                '}';
    }
}
