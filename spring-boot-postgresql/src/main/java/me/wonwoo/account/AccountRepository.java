package me.wonwoo.account;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Created by wonwoo on 2016. 3. 7..
 */
@Repository
public interface AccountRepository extends JpaRepository<Account, Long> {
}
