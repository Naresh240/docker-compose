package me.wonwoo.account;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * Created by wonwoo on 2016. 3. 7..
 */
@Slf4j
@RestController
public class AccountController {

    @Autowired
    private AccountRepository repository;

    @RequestMapping(value = "/accounts", method = RequestMethod.GET)
    public ResponseEntity<?> getAccount() {
        List<Account> accounts = repository.findAll();
        log.debug("accounts : {} ", accounts);
        return new ResponseEntity<>(accounts, HttpStatus.OK);
    }
}
