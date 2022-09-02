# Danny Radosevich
# Adapted from: https://ahsmart.com/pub/hacking_aes_ecb_mode_cipher/

string_to_hex(s) = [UInt8(x) for x in s]

function grouped(A; n = 16)
    s = length(A)
    [A[i:min(s,i+n-1) for i in 1:n:s]]
end

grouped(string_to_hex("HI"),n=4)