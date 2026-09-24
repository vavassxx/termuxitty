package com.termux.app;

import com.termux.shared.termux.TermuxConstants;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

/** Verifies that this build identifies itself as the Termuxitty fork. */
public class TermuxittyIdentityTest {
    @Test
    public void appNameIsTermuxitty() {
        assertEquals("Termuxitty", TermuxConstants.TERMUX_APP_NAME);
    }
}
