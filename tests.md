# SYNOPSIS

```raku
    use v6.d;
    use Test;
    use Test::Output;

    my &test-code = sub {
        say 42;
        note 'warning!';
        say "After warning";
    };

    # Test code's output using exact match ('is')
    output-is   &test-code, "42\nwarning!\nAfter warning\n", 'testing output';
    stdout-is   &test-code, "42\nAfter warning\n",  'testing stdout';
    stderr-is   &test-code, "warning!\n", 'testing stderr';

    # Test code's output using regex ('like')
    output-like &test-code, /42.+warning.+After/, 'testing output (regex)';
    stdout-like &test-code, /42/, 'testing stdout (regex)';
    stderr-like &test-code, /^ "warning!\n" $/, 'testing stderr (regex)';

    # Just capture code's output and do whatever you want with it
    is output-from( &test-code ), "42\nwarning!\nAfter warning\n";
    is stdout-from( &test-code ), "42\nAfter warning\n";
    is stderr-from( &test-code ), "warning!\n";

```
