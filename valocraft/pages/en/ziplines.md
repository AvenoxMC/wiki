# Ziplines


Ziplines are a map feature: a rope between two points that players can ride. They can be **horizontal, ascending or descending**.

## Riding a zipline (players)

| Action | Key |
|---|---|
| Hook on | **F**, near the rope |
| Slide | **Forward / backward**, in either direction depending on where you look |
| Let go | **Jump** or **sneak** |

- At the end of the rope, the player is dropped on the platform.
- You **can shoot** while riding.

## Creating a zipline (admins)

1. Get the wand: `/vc wand`.
2. **Left click** a block for point **A**, **right click** a block for point **B**. The points are the **centers of the clicked blocks**.
3. Run:

```
/vc map addzipline <map>
```

### Managing ziplines

```
/vc map ziplines <map>               list the ziplines
/vc map removezipline <map> <n>      remove zipline number n
```

## Technical notes

Each zipline is a **single display entity**, and movement is **interpolated client side**. It is smooth and cheap on the server.

See also [Map Setup](page:map-setup).
