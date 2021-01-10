package com.zoe.autoyqtb;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface Repo extends JpaRepository<User, Integer> {
    Optional<User> findByAccount(String account);
}
