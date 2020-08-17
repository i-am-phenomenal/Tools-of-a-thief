/*++

Module Name:

    public.h

Abstract:

    This module contains the common declarations shared by driver
    and user applications.

Environment:

    user and kernel

--*/

//
// Define an Interface Guid so that apps can find the device and talk to it.
//

DEFINE_GUID (GUID_DEVINTERFACE_KMDFDriver,
    0xe539da70,0x8899,0x4603,0x95,0xb8,0x16,0x69,0x47,0x08,0x17,0x95);
// {e539da70-8899-4603-95b8-166947081795}
