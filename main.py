# Compute Gravitational Blueshift #
# circum is ratio of circumference at which you hover above the hole #
#   to the circumference of the event horizon #
# lambdas is the wavelength of emitted light from star, meters #
# lambdar is the wavelength of received light, meters #
import math

lambdas = 5.8E-7  # Yellow light is 5.8E-7 meters
lambdar = 0
i = 0

print("C/Ch Lambda (emit) Lambda (rec)\n")

for j in range(21):
    circum = 1 + (0.5 ** i)
    i += 1
    lambdar = lambdas * math.sqrt(1.0 - (1.0 / circum))
    print(f"j={j}, Circum={circum} Lambdas={lambdas} Lambdar={lambdar}")
