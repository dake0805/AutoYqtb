package com.zoe.autoyqtb.vo;

import java.util.Objects;

public class AddUser {
    private String account;
    private String password;
    private String locationCode;
    private String locationName;
    private boolean inSchool;

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

    public String getLocationCode() {
        return locationCode;
    }

    public void setLocationCode(String locationCode) {
        this.locationCode = locationCode;
    }

    public String getLocationName() {
        return locationName;
    }

    public void setLocationName(String locationName) {
        this.locationName = locationName;
    }

    public boolean isInSchool() {
        return inSchool;
    }

    public void setInSchool(boolean inSchool) {
        this.inSchool = inSchool;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        AddUser addUser = (AddUser) o;
        return Objects.equals(account, addUser.account);
    }

    @Override
    public int hashCode() {
        return Objects.hash(account);
    }

    @Override
    public String toString() {
        return "AddUser{" +
                "account='" + account + '\'' +
                ", password='" + password + '\'' +
                ", locationCode='" + locationCode + '\'' +
                ", locationName='" + locationName + '\'' +
                ", inSchool=" + inSchool +
                '}';
    }
}
