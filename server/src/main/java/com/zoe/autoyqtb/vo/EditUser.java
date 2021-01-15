package com.zoe.autoyqtb.vo;

public class EditUser {
    private String account;
    private String oldPassword;
    private String newPassword;
    private String locationCode;
    private String locationName;
    private boolean inSchool;
    private boolean wantStop;

    public String getAccount() {
        return account;
    }

    public void setAccount(String account) {
        this.account = account;
    }

    public String getOldPassword() {
        return oldPassword;
    }

    public void setOldPassword(String oldPassword) {
        this.oldPassword = oldPassword;
    }

    public String getNewPassword() {
        return newPassword;
    }

    public void setNewPassword(String newPassword) {
        this.newPassword = newPassword;
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

    public boolean isWantStop() {
        return wantStop;
    }

    public void setWantStop(boolean wantStop) {
        this.wantStop = wantStop;
    }
}
